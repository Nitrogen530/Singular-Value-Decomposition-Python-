import math
import numpy as np
import time

print('''1) USE SPACE TO DIFF B/W COLOUM
2) DO NOT LEAVE SPACE AFTER THE LAST DIGIT OF YOUR COLOUM
''')


def mat_input(number_rows):  # generalised input
    try:
        main_list = []
        print('NOTE : no limit for coloum')
        user_row_input = 0
        row_counter = 1
        while user_row_input < number_rows:
            coloum_capture = []
            colom_mat_inp = input(f'row {row_counter} > ').split(' ')
            user_row_input += 1
            row_counter += 1
            for var in colom_mat_inp:
                coloum_capture.append(int(var))
            main_list.append(coloum_capture)
        return main_list
    except ValueError:
        print('make sure there are no space after last digit of your row and no alphabets are present')
        time.sleep(0.2)
        return mat_input()
user_in = int(input('No of rows > '))
# mat_out can be used for futher programming
mat_out = mat_input(user_in)
# matrix copier for further use


def matrix_copier(mat_out):  # generalised copier
    mat_out_len = len(mat_out)
    n = 0
    Empt_list = []
    while n < mat_out_len:
        for i in range(mat_out_len):
            Empt_list.append(mat_out[i])
            n += 1
    return Empt_list
copy_of_original = matrix_copier(mat_out)

A = np.array(mat_out)
print("\n\n\n Matrix A: \n", A, sep="")
AT = A.transpose()
print("\n\n\n Transpose of Matrix A: \n", AT, sep="")
AAT = A@AT
print("\n\n\n Matrix AAT: \n", AAT, sep="")
ATA = AT@A
print("\n\n\n Matrix ATA: \n", ATA, sep="")

# SOlVING FOR EIGENVALUES OF ATA FOR NOW:
ATA_a = 1
ATA_b = -(ATA[0][0] + ATA[1][1])
ATA_c = ((ATA[0][0] * ATA[1][1]) - (ATA[1][0] * ATA[0][1]))

ATA_L1 = (-(ATA_b) + (math.sqrt((ATA_b**2) - 4 * (ATA_c)))) / 2 * ATA_a
ATA_L2 = (-(ATA_b) - (math.sqrt((ATA_b**2) - 4 * (ATA_c)))) / 2 * ATA_a

print("\n\n\nThe lambda values for ATA :")
print(ATA_L1)
print(ATA_L2)

# SOlVING FOR EIGENVALUES OF AAT FOR NOW (JUST FOR CONFIRMATION):

AAT_a = 1
AAT_b = -(AAT[0][0] + AAT[1][1])
AAT_c = ((AAT[0][0] * AAT[1][1]) - (AAT[1][0] * AAT[0][1]))

AAT_L1 = -((AAT_b) + math.sqrt((AAT_b**2) - 4 * (AAT_c))) / (2 * AAT_a)
AAT_L2 = -((AAT_b) - math.sqrt((AAT_b**2) - 4 * (AAT_c))) / (2 * AAT_a)

print("\n\n\nThe lambda values for AAT :")
print(AAT_L1)
print(AAT_L2)

# Values for Sigma Matrix, might need changes upon clarification of definitions
Sig1 = math.sqrt(AAT_L1)
Sig2 = math.sqrt(AAT_L2)

E = np.array([[Sig1, 0], [0, Sig2]])  # Diagonal Matrix Sigma

print("\n\n\n Matrix Sigma (E): \n", E, sep="")
# SOLVING FOR EIGEN VECTORS OF ATA :
# SOLVING FOR L1:

ATA_p1 = ATA[0][0] - ATA_L1
ATA_q1 = ATA[0][1]
ATA_r1 = ATA[1][0]
ATA_s1 = ATA[1][1] - ATA_L1

ATA_A1 = np.array([[ATA_p1, ATA_q1], [ATA_r1, ATA_s1]])
ATA_B1 = np.array([[0, 0], [0, 0]])


# SOLVING SIMULATANEOUS EQUATION:   !! RETURNS -0,-0 always !!


#AA_T_V1 = np.linalg.solve(AAT_A1,AAT_B1)
AAT_a1 = AAT[0][0] - AAT_L2
AAT_b1 = AAT[0][1]
AAT_c1 = AAT[1][0]
AAT_d1 = AAT[1][1] - AAT_L2

AAT_A1 = np.array([[AAT_a1, AAT_b1], [AAT_c1, AAT_d1]])
AAT_B1 = np.array([[0, 0], [0, 0]])

ATA_V1 = np.linalg.eig(ATA_A1)
AAT_V2 = np.linalg.eig(AAT_A1)


# ATA_V2=np.linalg.eig(ATA_B1)
print("\n\n\n\nSolutions of eq. 1 :\n", ATA_V1[1])
print("\n\n\n\nSolutions of eq. 1 2 :\n", AAT_V2[2])
