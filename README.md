### Program Name : Enigma-Machine-Simulator
#### Author : M.Fatih Altuntaş
#### Description : This is a simulator of enigma machine(m3) on python, it runs exactly same real enigma machine

This simulators  implemented based on enigma m3 machine, below image shows it
![full](https://cloud.githubusercontent.com/assets/13722649/26524895/ff527d84-434d-11e7-9488-2e8f10d522f1.jpg)


Extra information about machine such as properties , how it works and egg...[Please go to this link](http://www.cryptomuseum.com/crypto/enigma/m3/index.htm)
<br />

##### How to run

```
python3 enigma.py -m ENIGMA -sp KET -n2 E -n3 V 
```
<br />Argumets
* -m plaintext
* -sp,Initial positons of rotors,for above rotor1=K,rotor2=E and rotor3=T
* -n2,notch positon of rotor2
* -n1,notch positon of rotor2
* -r,reflactor,

<br />Output
```
Fatihs-MacBook-Pro:Enigma fatih$ python3 enigma.py -m ENIGMA -sp KET -n2 E -n3 V 
Running
Message is  ENIGMA
Initial posion of rotor  KET
Notch posion of rotor3 and rotor2  V E
------------------------------------------------------------------------------------------------------------------------
Enigma : ENIGMA  ->  HUBNEQ
```
<br />For  revert plaintext,you can run  script  again with same config, as follows

```
Fatihs-MacBook-Pro:Enigma fatih$ python3 enigma.py -m HUBNEQ -sp KET -n2 E -n3 V 
Running
Message is  HUBNEQ
Initial posion of rotor  KET
Notch posion of rotor3 and rotor2  V E
------------------------------------------------------------------------------------------------------------------------
Enigma : HUBNEQ  ->  ENIGMA
```


<br />Detailed outputs as follows,it show each steps of proccesing


```
Fatihs-MacBook-Pro:Enigma fatih$ python3 enigma.py -m CYBERSTRUGGLE -sp CSR -n2 E -n3 V 
Running
Message is  CYBERSTRUGGLE
Initial posion of rotor  CSR
Notch posion of rotor3 and rotor2  V E
------------------------------------------------------------------------------------------------------------------------
Input is : C
Push  rotor3 :  C -> K
Push  rotor2 :  S -> L
Push  rotor1 :  T -> I
Reflactor B: I -> N
Reverseee Start 
Reverse Directoin in rotor1 : N -> A
Reverse Directoin in rotor2 : A -> A
Reverse Directoin in rotor3 : A -> B
Output is : B
------------------------------------------------------------------------------------------------------------------------
Input is : Y
Push  rotor3 :  Y -> W
Push  rotor2 :  D -> Y
Push  rotor1 :  G -> V
Reflactor B: V -> B
Reverseee Start 
Reverse Directoin in rotor1 : B -> M
Reverse Directoin in rotor2 : M -> P
Reverse Directoin in rotor3 : P -> O
Output is : O
------------------------------------------------------------------------------------------------------------------------
Input is : B
Push  rotor3 :  B -> M
Push  rotor2 :  S -> L
Push  rotor1 :  T -> I
Reflactor B: I -> N
Reverseee Start 
Reverse Directoin in rotor1 : N -> A
Reverse Directoin in rotor2 : A -> C
Reverse Directoin in rotor3 : C -> M
Output is : M
------------------------------------------------------------------------------------------------------------------------
Input is : E
Push  rotor3 :  E -> O
Push  rotor2 :  T -> H
Push  rotor1 :  P -> U
Reflactor B: U -> H
Reverseee Start 
Reverse Directoin in rotor1 : H -> F
Reverse Directoin in rotor2 : F -> Z
Reverse Directoin in rotor3 : Z -> R
Output is : R
------------------------------------------------------------------------------------------------------------------------
Input is : R
Push  rotor3 :  R -> N
Push  rotor2 :  R -> L
Push  rotor1 :  S -> A
Reflactor B: A -> C
Reverseee Start 
Reverse Directoin in rotor1 : C -> P
Reverse Directoin in rotor2 : P -> X
Reverse Directoin in rotor3 : X -> O
Output is : O
------------------------------------------------------------------------------------------------------------------------
Input is : S
Push  rotor3 :  S -> E
Push  rotor2 :  H -> A
Push  rotor1 :  H -> Z
Reflactor B: Z -> L
Reverseee Start 
Reverse Directoin in rotor1 : L -> V
Reverse Directoin in rotor2 : V -> B
Reverse Directoin in rotor3 : B -> D
Output is : D
------------------------------------------------------------------------------------------------------------------------
Input is : T
Push  rotor3 :  T -> W
Push  rotor2 :  Y -> G
Push  rotor1 :  N -> H
Reflactor B: H -> U
Reverseee Start 
Reverse Directoin in rotor1 : U -> I
Reverse Directoin in rotor2 : I -> K
Reverse Directoin in rotor3 : K -> W
Output is : W
------------------------------------------------------------------------------------------------------------------------
Input is : R
Push  rotor3 :  R -> I
Push  rotor2 :  J -> D
Push  rotor1 :  K -> O
Reflactor B: O -> Q
Reverseee Start 
Reverse Directoin in rotor1 : Q -> Y
Reverse Directoin in rotor2 : Y -> B
Reverse Directoin in rotor3 : B -> B
Output is : B
------------------------------------------------------------------------------------------------------------------------
Input is : U
Push  rotor3 :  U -> K
Push  rotor2 :  K -> K
Push  rotor1 :  R -> P
Reflactor B: P -> M
Reverseee Start 
Reverse Directoin in rotor1 : M -> T
Reverse Directoin in rotor2 : T -> U
Reverse Directoin in rotor3 : U -> W
Output is : W
------------------------------------------------------------------------------------------------------------------------
Input is : G
Push  rotor3 :  G -> P
Push  rotor2 :  O -> U
Push  rotor1 :  B -> F
Reflactor B: F -> J
Reverseee Start 
Reverse Directoin in rotor1 : J -> Q
Reverse Directoin in rotor2 : Q -> Y
Reverse Directoin in rotor3 : Y -> N
Output is : N
------------------------------------------------------------------------------------------------------------------------
Input is : G
Push  rotor3 :  G -> R
Push  rotor2 :  P -> X
Push  rotor1 :  E -> D
Reflactor B: D -> T
Reverseee Start 
Reverse Directoin in rotor1 : T -> C
Reverse Directoin in rotor2 : C -> Y
Reverse Directoin in rotor3 : Y -> M
Output is : M
------------------------------------------------------------------------------------------------------------------------
Input is : L
Push  rotor3 :  L -> Y
Push  rotor2 :  V -> M
Push  rotor1 :  T -> I
Reflactor B: I -> N
Reverseee Start 
Reverse Directoin in rotor1 : N -> B
Reverse Directoin in rotor2 : B -> T
Reverse Directoin in rotor3 : T -> G
Output is : G
------------------------------------------------------------------------------------------------------------------------
Input is : E
Push  rotor3 :  E -> R
Push  rotor2 :  N -> R
Push  rotor1 :  Y -> E
Reflactor B: E -> W
Reverseee Start 
Reverse Directoin in rotor1 : W -> E
Reverse Directoin in rotor2 : E -> K
Reverse Directoin in rotor3 : K -> Q
Output is : Q
------------------------------------------------------------------------------------------------------------------------
Enigma : CYBERSTRUGGLE  ->  BOMRODWBWNMGQ

```
