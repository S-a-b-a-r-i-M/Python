#EXCEPTIONS....AND HANDLING

print("exception handling".title())
animal="lion"
'''
try:
    nom=int(input('Enter nominator:'))
    denom=int(input('Enter denominator:'))
    cotient=nom/denom
    print(animal[9])    #INDEX OUT OF RANGE

except ZeroDivisionError as err:
    print(err)

except: # Exception: #CATCH
    print("Error occured")

else:       #IT WILL EXECUTE WHEN THERE IS NO EXCEPTION
    print("res :",cotient)

finally:      #ALWAYS EXECUTES
    print("Margaya sala......")
'''

def is_eligible(age):
    try:
        if age<18:
            raise Exception('You are too young to vote...so rejected')
    except Exception as err:
        print(err)
    else:
        print("You are eligible to vote")


is_eligible(0)