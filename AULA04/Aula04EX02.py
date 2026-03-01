A, B, C = map(int, input("Digite 3 números").split())

if A > B and A > C:
    if B > C:
        print(f"{A}, {B}, {C}")
    else:
        print(f"{A}, {C}, {B}")

elif B > A and B > C:
    if A > C:
        print(f"{B}, {A}, {C}")
    else:
        print(f"{B}, {C}, {A}")

elif C > A and C > B:
    if A > B:
        print(f"{C}, {A}, {B}")
    else:
        print(f"{C}, {B}, {A}")

 