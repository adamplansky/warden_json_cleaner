def handle: inputs| select([.Category[]  != "Test"] | all) | (.DetectTime|tostring) + "\t" + (.|tostring);
def process: try handle catch ( process) ;
process
