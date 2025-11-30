def groupangrams(words):
    results ={}
    
    for w in words:
        key ="".join(sorted(w))
        
        if key not in results:
            results[key] = []
            
        results[key].append(w)
        
    return list(results.values())
    
print(groupangrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
