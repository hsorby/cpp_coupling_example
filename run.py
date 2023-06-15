import os
from libcellml import Analyser, AnalyserModel, AnalyserExternalVariable, Generator, GeneratorProfile, \
                      Parser, Importer

def resolve_imports(model, base_dir, strict_mode):
    importer = Importer(strict_mode)
    importer.resolveImports(model, base_dir)
    _dump_issues("resolve_imports", importer)
    if model.hasUnresolvedImports():
        print("unresolved imports?")
    else:
        print("no unresolved imports.")
    return importer

def parse_model(filename, strict_mode):
    cellml_file = open(filename)
    parser = Parser(strict_mode)
    model = parser.parseModel(cellml_file.read())
    _dump_issues("parse_model", parser)
    return model

def flatten_model(model, importer):
    flat_model = importer.flattenModel(model)
    return flat_model

def _dump_issues(source_method_name, logger):
    if logger.issueCount() > 0:
        print('The method "{}" found {} issues:'.format(source_method_name, logger.issueCount()))
        for i in range(0, logger.issueCount()):
            print('    - {}'.format(logger.issue(i).description()))

model_dir = os.path.dirname(__file__) 
model_name = 'cpp_coupling'
model_file_path = os.path.join(model_dir, model_name + '.cellml')

# parse the model in non-strict mode to allow non CellML 2.0 models
model = parse_model(model_file_path, False)
model_dir = os.path.dirname(model_file_path)

# code for importing the modules, parameters, and units, files.

# resolve imports, in non-strict mode
importer = resolve_imports(model, model_dir, False)
print("model.hasUnresolvedImports() = {}".format(model.hasUnresolvedImports()))
# need a flattened model for analysing
flat_model = flatten_model(model, importer)

# create model analyser
a = Analyser()

# add some external variables etc here, for this example case do nothing

# analyse the model
a.analyseModel(flat_model)

analysed_model = a.model()
print(f"Analysed model type: {analysed_model.type()}")
if not analysed_model.isValid():
    _dump_issues("analyse_model", a)
    print("model is not valid, aborting...")
    exit()


g = Generator()
g.setModel(a.model())
profile = GeneratorProfile(GeneratorProfile.Profile.PYTHON)
g.setProfile(profile)

implementation_code_python = g.implementationCode()
with open(f"{model_name}.py", "w") as f:
    f.write(implementation_code_python)

