# main.py

import argparse
from utils.api_client import fetch_data
from utils.formatter import *
from toolkit.analyzer import *
from utils.file_handler import *

def main():
    parser = argparse.ArgumentParser(
        description="API Data Analyzer CLI"
    )
    parser.add_argument("--endpoint", required=True, choices=["posts", "comments", "users"])
    parser.add_argument("--user", type=int)
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--export", type=str)
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()
    
    params = {}
    if args.user is not None and args.endpoint in ["posts", "comments"]:
        params["userId"] = args.user
        
    data = fetch_data(args.endpoint, params)
    if data is None:
        return
    
    if args.summary:
        summary = get_summary(args.endpoint, data)
        print_summary(summary)
    
    print_records(args.endpoint, data, args.limit)
    
    if args.export:
        export_to_json(data, args.export)
    
if __name__ == "__main__":
    main()
    