from icoscp.cpb.dobj import Dobj

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




uri = 'https://meta.icos-cp.eu/objects/3ustUwkTykY3-170p0SvPUXw'
dobj = Dobj(uri)

file_dobj = open("/tmp/dobj_" + id + ".json", "w")
file_dobj.write(json.dumps(dobj))
file_dobj.close()
