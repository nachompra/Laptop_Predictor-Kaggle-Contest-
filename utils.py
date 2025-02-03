import re

def extract_total_memory(storage_string):
    total_gb = 0
    
    gb_pattern = r'(\d+(?:\.\d+)?)\s*GB'
    tb_pattern = r'(\d+(?:\.\d+)?)\s*TB'
    
    gb_matches = re.findall(gb_pattern, storage_string, flags=re.IGNORECASE)
    tb_matches = re.findall(tb_pattern, storage_string, flags=re.IGNORECASE)

    for match in gb_matches:
        total_gb += float(match)

    for match in tb_matches:
        total_gb += float(match) * 1024
    
    return total_gb

def opsys_classifier(opsys):
    if 'Windows' in opsys:
        return 'Windows'
    elif 'Linux' in opsys:
        return 'Linux'
    elif 'mac' in opsys.lower():
        return 'Mac'
    else:
        return opsys
    
def opsys_get_version(opsys):
    if 'Windows' in opsys:
        match = re.search(r'Windows\s*([\d\.]+)', opsys, re.IGNORECASE)
        if match:
            return match.group(1)
        else:
            return 'Windows'
    elif 'mac' in opsys.lower():
        # we lower the str to ensure performance
        opsys_lower = opsys.lower()
        if 'mac os' in opsys_lower:
            return 1 #mac os refers to olders version of the opsys
        elif 'macos' in opsys_lower:
            return 2 #macos referes to newers ones which may be more expensive
        else:
            return None 
    else:
        return 0
    
from fuzzywuzzy import process
def fuzzy_match_gpu(gpu_name, gpu_map, threshold=90):
    # Find the best match from gpu_map keys using fuzzywuzzy's process.extractOne
    best_match, score = process.extractOne(gpu_name.lower(), gpu_map.keys())
    if score >= threshold:  # Match is considered valid if score is above the threshold
        return gpu_map[best_match]
    else:
        return 0  # If no good match, return 0