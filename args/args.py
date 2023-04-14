def concatenate_args(*string):
    answer= " "
    for s in string:
        answer+=s
    return answer


def concatenate_kwargs(**string):
    empty= ""
    for key, value in string.items():
        empty+=(f"{key}{value}")
    return empty





