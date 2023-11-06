import click

def fibb_seq(n: int):
    k = [0] * n
    k[1] = 1 #Bumping up the second element to one.
    for i in range(1, n):
        if i >= 2:
            k[i] = k[i-2] + k[i-1]
    return k

@click.command(context_settings={"show_default": True})
@click.option("--example", "-e", help="Example showing click usage", type=str)
@click.option("-n", help="Index of the Fibbonacci sequence", type=int)
def main(example: str, n: int):
    """Explain your function here"""
    print(example)
    print(fibb_seq(n))

if __name__ == "__main__":
    main()
