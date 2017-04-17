import fixedMagFuncs as fmf

def main():

    stArr = fmf.SameMagStates(2,3)
    # print(stArr)

    print(fmf.magBlockHamiltonian(stArr,3))


if __name__ == '__main__':
    main()
