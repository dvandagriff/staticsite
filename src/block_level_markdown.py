

def markdown_to_blocks(md):
    return [
        i.strip().strip('\n')
        for i in md.split('\n\n')
    ]
