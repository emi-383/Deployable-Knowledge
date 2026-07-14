import os
import pathlib
from beir import util

# Datasets and what they test:
# "scifact" - scientific, technical, or fact verification
# "hotpotqa" - multihop reasoning
# "nfcorpus" - TREC-Covid: biomedical terminology
# "nq" - Natural Questions: simulate real user general queries

# Change below to adjust dataset used:
DATASET_TYPE: str = "scifact"
# ============================================================

def seed_dataset(script_dir: pathlib.Path) -> str:
    '''Prepare folder and beir dataset'''

    # Root folder pointer
    data_dir = os.path.join(script_dir, "data")
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    else:
        print(f"'{data_dir}' already exists------------")
    
    url = f"https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/{DATASET_TYPE}.zip"
    
    print(f"Starting download and seed '{DATASET_TYPE}' dataset")
    # Extract the zip into new folder
    data_path = util.download_and_unzip(url, data_dir)
    print(f"Done at: {data_path}")
    return data_path

def py_to_ts(script_dir: pathlib.Path) -> None:
    '''Store dataset_type in active_dataset.txt for prep_benchmark.ts to read'''

    transfer_path = os.path.join(script_dir, "active_dataset.txt")
    
    with open(transfer_path, "w", encoding="utf-8") as f:
        f.write(DATASET_TYPE)
        
    print(f"Dataset '{DATASET_TYPE}' written to {transfer_path}")
    

if __name__ == "__main__":
    print(f'Current dataset type: {DATASET_TYPE}')
    try:
        script_dir = pathlib.Path(__file__).parent.absolute()
        seed_dataset(script_dir)
        py_to_ts(script_dir)
    except Exception as e:
        print(f"\nData loading failed: {e}")
        exit(1)