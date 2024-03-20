def main(N):
    return f"The return number is now : {N+3}"

n = 3000

def usd_to_riels(x):
    return f"\n[i] \t{x} \tUSD \t= \t{4053 * x} Riels\n"

def riels_to_usd(x):
    return f"\n[i] \t{x} \tRiels \t= \t{x / 4053} USD\n"


print(usd_to_riels(1))
print(riels_to_usd(10000))