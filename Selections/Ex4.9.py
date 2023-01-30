# Below is the programming exercise
# (Financial: compare costs) Suppose you shop for rice and find it in two differentsized
# packages. You would like to write a program to compare the costs of the
# packages. The program prompts the user to enter the weight and price of each
# package and then displays the one with the better price.

# Prompts user to type in the weight and price of each package
weight1=eval(input("Type in the weight of package 1: "))
price1=eval(input("Type in the price of package 1: "))
weight2=eval(input("Type in the weight of package 2: "))
price2=eval(input("Type in the price of package 2: "))

package1=weight1/price1
package2=weight2/price2

if package1>package2:
    print("Package 1 has the better price.")
else:
    print("Package 2 has the better price.")