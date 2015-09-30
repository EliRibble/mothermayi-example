def plugin():
    return {
        'name'          : 'example',
        'pre-commit'    : pre_commit,
    }

def pre_commit(config, staged):
    lines = ["  {}...looks nice".format(s) for s in staged]
    return "\n".join(lines)
