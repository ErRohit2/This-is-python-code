# Make a string in three types : -
# ======================================>
name ="Rohit Kumar Sahu "
print(name)

name= ' Rohit '
print(name)

name='''harshit '''
print(name)

print(name[2])   # 2 means 3rd positiont ;; number start with 0  print r 
print(name[0:4]) # print hars !!

# name.strip()  :- remove the spaces in string
# =======================> 
   
# for eg :- 
name2="      Rohit Bhai     "
print(name2)  # print with space asitige print :-     Rohit Bhai     ..
# but :-
print(name2.strip())  # remove spaces in name print :- Rohit Bhai


# Lentgth Of String :- 
# ===========================>
namee = "JAMUNA"
print(len(namee)) # print 6

# lower() case and upper() case :- 
# ================================>

var = namee.lower()
print(var)   #  print :-  jamuna

vari = var.upper()
print(vari)  #print :- JAMUNA

# Replace Functon :- 
# ===========================>

# for eg :- 

rip = namee.replace(" A " ,"M")
print(rip)

# for eg :- 

#replace (  , symbol  )
# ===========================>
 
nameee = "Rohit , Harshit , Ashish"
varr =nameee.replace("," , '\n')
print(varr)

# Add Two Srring : -
# ========================>

# for eg ;
stri1 = "This Is A " 
stri2 ="Rohit Kumar Sahu"
print(stri1 +stri2)

# Make A Template Placeholder {} : -
# =========================================>
# {} = placeholder : change {0} or {1} or {2} replace for other name :- 
#  f"   {} {} "  ->  fstring

name11 = "Rohit"
name12 = "Jamuna Prasad"

#  Two ways :- 
# ------------------->

# Temp ="This is son of {}  and the name of student is {} ".format(name12 ,name11)
Temp =f"This is son of {name12}  and the name of student is {name12}"
print(Temp)

# Quiz : - Try this oprator :- 
# =====================================>

# **  => xponentiation operator ;
# //  => floor division operator ;
# %   => modulo operator

