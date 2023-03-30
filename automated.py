#for 1 frame 
"""
angle = 0.00
for i in range(100):
    angle="{:.2f}".format(angle)

    #color: yellow and black
    # print(str(i)+"%", "{", f'background-image: conic-gradient(from {angle}deg, #f5fe01, #69685c);', "}")

    # color: lavender and light lavender
    print(str(i)+"%", "{", f'background-image: conic-gradient(from {angle}deg, #7b2cbf, #e0aaff);', "}")

    angle = float(angle)+3.6
"""

# """
#for 0.5 frames
# angle = 0.00
# a = 0.00
# for i in range(200):
#     angle="{:.2f}".format(angle)

#     #color: yellow and black
#     print(str(i)+"%", "{", f'background-image: conic-gradient(from {angle}deg, #504f51, #000);', "}")

#     # color: lavender and light lavender
#     # print(str(a)+"%", "{", f'background-image: conic-gradient(from {angle}deg, #504f51, #000);', "}")

#     angle = float(angle)+1.8
#     a+=0.5
# """

"""
# #for 0.5 frames but 3 colors
angle = 0.00
a = 0.00
for i in range(200):
    angle="{:.2f}".format(angle)

    #color: yellow and black
    # print(str(i)+"%", "{", f'background-image: conic-gradient(from {angle}deg, #f5fe01, #69685c);', "}")

    # color: lavender and light lavender
    print(str(a)+"%", "{", f'background-image: conic-gradient(from {angle}deg, #1c1a1a, #1c1a1a, #1c1a1a, #504f51);', "}")

    angle = float(angle)+1.8
    a+=0.5
    """

# angle = 0.00
# a = 0.00
# for i in range(200):
    # angle="{:.2f}".format(angle)

    #color: yellow and black
    # print(str(i)+"%", "{", f'background-image: conic-gradient(from {angle}deg, #f5fe01, #69685c);', "}")

    # color: lavender and light lavender
    # print(str(a)+"%", "{", f'background-image: conic-gradient(from {angle}deg, #1c1a1a, #1c1a1a, #1c1a1a, #504f51);', "}")

    # angle = float(angle)+1.8
    # if angle>=276:
    #     print(str(a)+"%","{color: red;}")
    # if a== 99.5:
    #     break

    # if angle>=40:
    #     print(str(a)+"%", "{color: #1c1a1a;}")
    # if angle==76.0:
    #     break
    # else:
    #     print(str(a)+"%", "{color: #1c1a1a}")
    # a+=0.5


# For "College" animation color change
# angle = 0.00
# a = 0.00
# for i in range(200):
#     angle="{:.2f}".format(angle)
#     angle = float(angle)+1.8
#     if a>=0 and a<=10.5:
#         print(str(a)+"%", "{color: #FFA511}")
#     elif a>=11 and a<=78.5:
#         print(str(a)+"%", "{color: #1c1a1a;}")
#     elif a>=79 and a<=99.5:
#         print(str(a)+"%", "{color: #FFA511;}")
#     a+=0.5

# for image color change animation
angle = 0.00
a = 0.00
for i in range(200):
    angle="{:.2f}".format(angle)
    angle = float(angle)+1.8
    if angle>=78 and angle<=228:
        print(str(a)+"%", "{opacity: 1}")
    else:
        print(str(a)+"%", "{opacity: 0}")
    a+=0.5