<p align="center">
  <img src="https://user-images.githubusercontent.com/73163292/96565392-edb5fa80-12e1-11eb-83ff-96165e14688f.png" width="154">
  <h1 align="center">Simple Calculator</h1>
  <p align="center">A <b>calculator</b> with the basic functions and a customizable, implemented in Python.</p>
  
  <p align="center">
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
    <a href="https://github.com/cipherML">
    	<img src="https://img.shields.io/badge/Author-Mayur%20Pawar-lightgrey" />
    </a>
    
    
## Table of contents
- [How to download or clone](#Clone)
- [Mathematical operations](#Mathematical-Operations)
- [Module Examples](#Module-examples)
  * [Addition](#Module-examples)
  * [Subtraction](#Module-examples)
  * [Multiplication](#Module-examples)
  * [Division](#Module-examples)
  * [Power](#Module-examples)
  * [Square-root](#Module-examples)
  * [Modulus](#Module-examples)
- [Run](#Run)

## **Clone**
Run this in your terminal: 

`https://github.com/cipherML/Simple-Calculator-python.git`

__Important:__ 
**Python 3.6 or 3.7** is needed to run the toolbox.
- IDE `Pycharm`

### **Mathematical Operations**
-    Addition (+) 
-    Subtraction (-)
-    Multiplication (*)
-    Division (/)
-    Power (^) ")
-    Square-root (&)
-    mod (%)
-   floor div (//)
 
### **Module examples**
**Addition**

    Calulator: 14+77
    ans= :  91.0
**Multiplication**

    Calulator: 11*5
    ans= :  55.0
**Power**

    Calulator: 10^3
    ans= :  1000.0
**Square-root**

    Calulator: 49&
    ans= :  7.0
**mod**

    Calulator: 51%5
    ans= :  1,0
    
## **Run**
```python

from myCalculator import TheCalculator

exe = TheCalculator()
try:
    while True:
        ans = exe.calc(input("Calculator:"))
        print("ans= : ", ans)
except KeyboardInterrupt:
    print("\n\n Thank You.! Have a Good Day")
```
