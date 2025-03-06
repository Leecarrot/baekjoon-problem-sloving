def solution(new_id):
    alpha = 'abcdefghijklmnopqrstuwvxyz0123456789-_.'
    new_id1 = new_id.lower()
    
    new_id2 = ''
    
    for w in new_id1:
        if w in alpha:
            new_id2 += w
            
    new_id3 = ''
    for i in range(len(new_id2)):
        if i == 0 or not (new_id2[i] == '.' and new_id2[i-1] == '.'):
            new_id3 += new_id2[i]
    
    if new_id3 and new_id3[0] == '.':
        new_id3 = new_id3[1:]
    if new_id3 and new_id3[-1] == '.':
        new_id3 = new_id3[:-1]

    
    if not new_id3:
        new_id3 += 'a'
    
    if len(new_id3) >= 16:
        new_id3 = new_id3[:15]
        if new_id3[-1] == '.':
            new_id3 = new_id3[:-1]
            
    if len(new_id3) <= 2:
        while len(new_id3) < 3:
            new_id3 += new_id3[-1]
            
    return new_id3
            
            
        




        