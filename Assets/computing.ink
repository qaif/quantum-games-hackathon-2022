=== computing ===
VAR left=false
VAR middle=false
VAR right=false


VAR row_one_operation="none"
VAR row_two_operation="none"
VAR row_three_operation="none"

VAR row_one_target="none"
VAR row_two_target="none"
VAR row_three_target="none"

VAR row_one_control="none"
VAR row_two_control="none"
VAR row_three_control="none"
-> circuit

=circuit
The first row has {row_one_operation} to be done to {row_one_target} with control by {row_one_control}
The second row has {row_two_operation} to be done to {row_two_target} with control by {row_two_control}
The third row has {row_three_operation} to be done to {row_three_target} with control by {row_three_control}

+Fiddle with row 1
     Row 1 is doing {row_one_operation} to {row_one_target} with control by {row_one_control}
     ++ Change operation
           +++ Nothing (identity)
                   ~ row_one_operation="none"
           +++ Flip (X gate)
                   ~ row_one_operation="X"
           +++ Up phase differential (Z gate)
                   ~ row_one_operation="Z"
           +++ The superposition operator (Hadamar)
                   ~ row_one_operation="H"
           +++ The one operation that doesn't get used (Y gate)
                   ~ row_one_operation="Y"
     ++ Change target
           +++ left
                   ~ row_one_target="left"
           +++ middle
                   ~ row_one_target="middle"
           +++ right
                   ~ row_one_target="right"
     ++ Change control
           +++ left
                   ~ row_one_control="left"
           +++ middle
                   ~ row_one_control="middle"
           +++ right
                   ~ row_one_control="right"
+Fiddle with row 2
     ++ Change operation
           +++ Nothing (identity)
                   ~ row_two_operation="none"
           +++ Flip (X gate)
                   ~ row_two_operation="X"
           +++ Up phase differential (Z gate)
                   ~ row_two_operation="Z"
           +++ The superposition operator (Hadamar)
                   ~ row_two_operation="H"
           +++ The one operation that doesn't get used (Y gate)
                   ~ row_two_operation="Y"
     ++ Change target
           +++ left
                   ~ row_two_target="left"
           +++ middle
                   ~ row_two_target="middle"
           +++ right
                   ~ row_two_target="right"
     ++ Change control
           +++ left
                   ~ row_two_control="left"
           +++ middle
                   ~ row_two_control="middle"
           +++ right
                   ~ row_two_control="right"
+Fiddle with row 3
     ++ Change operation
           +++ Nothing (identity)
                   ~ row_three_operation="none"
           +++ Flip (X gate)
                   ~ row_three_operation="X"
           +++ Up phase differential (Z gate)
                   ~ row_three_operation="Z"
           +++ The superposition operator (Hadamar)
                   ~ row_three_operation="H"
           +++ The one operation that doesn't get used (Y gate)
                   ~ row_three_operation="Y"
     ++ Change target
           +++ left
                   ~ row_three_target="left"
           +++ middle
                   ~ row_three_target="middle"
           +++ right
                   ~ row_three_target="right"
     ++ Change control
           +++ no control
                   ~ row_three_control="none"
           +++ left
                   ~ row_three_control="left"
           +++ middle
                   ~ row_three_control="middle"
           +++ right
                   ~ row_three_control="right"
+Check result
     ->RunCircuit
+Leave
-
->circuit


=RunCircuit
Start with {left},{middle},{right}
{row_one_operation != "none":
{row_one_control=="left":
       {left==true:
               {row_one_operation=="X":
                       ~ degreeXGate(row_one_target,"0.5")
               }
               {row_one_operation=="Z":
                       ~ degreeZGate(row_one_target,"0.5")
               }
               {row_one_operation=="Y":
                       ~ degreeYGate(row_one_target,"0.5")
               }
               {row_one_operation=="H":
                       ~ splitWorld(row_one_target)
               }
       }:
}

{row_one_control=="middle":
       {middle==true:
               {row_one_operation=="X":
                       ~ degreeXGate(row_one_target,"0.5")
               }
               {row_one_operation=="Z":
                       ~ degreeZGate(row_one_target,"0.5")
               }
               {row_one_operation=="Y":
                       ~ degreeYGate(row_one_target,"0.5")
               }
               {row_one_operation=="H":
                       ~ splitWorld(row_one_target)
               }
       }:
}

{row_one_control=="right":
       {right==true:
               {row_one_operation=="X":
                       ~ degreeXGate(row_one_target,"0.5")
               }
               {row_one_operation=="Z":
                       ~ degreeZGate(row_one_target,"0.5")
               }
               {row_one_operation=="Y":
                       ~ degreeYGate(row_one_target,"0.5")
               }
               {row_one_operation=="H":
                       ~ splitWorld(row_one_target)
               }
       }:
}

{row_one_control=="none":
               {row_one_operation=="X":
                       ~ degreeXGate(row_one_target,"0.5")
               }
               {row_one_operation=="Z":
                       ~ degreeZGate(row_one_target,"0.5")
               }
               {row_one_operation=="Y":
                       ~ degreeYGate(row_one_target,"0.5")
               }
               {row_one_operation=="H":
                       ~ splitWorld(row_one_target)
               }
}
}

Step 1 state is {left},{middle},{right}
{row_two_operation != "none":
{row_two_control=="left":
       {left==true:
               {row_two_operation=="X":
                       ~ degreeXGate(row_two_target,"0.5")
               }
               {row_two_operation=="Z":
                       ~ degreeZGate(row_two_target,"0.5")
               }
               {row_two_operation=="Y":
                       ~ degreeYGate(row_two_target,"0.5")
               }
               {row_two_operation=="H":
                       ~ splitWorld(row_two_target)
               }
       }:
}
{row_two_control=="middle":
       {middle==true:
               {row_two_operation=="X":
                       ~ degreeXGate(row_two_target,"0.5")
               }
               {row_two_operation=="Z":
                       ~ degreeZGate(row_two_target,"0.5")
               }
               {row_two_operation=="Y":
                       ~ degreeYGate(row_two_target,"0.5")
               }
               {row_two_operation=="H":
                       ~ splitWorld(row_two_target)
               }
       }:
}
{row_two_control=="right":
       {right==true:
               {row_two_operation=="X":
                       ~ degreeXGate(row_two_target,"0.5")
               }
               {row_two_operation=="Z":
                       ~ degreeZGate(row_two_target,"0.5")
               }
               {row_two_operation=="Y":
                       ~ degreeYGate(row_two_target,"0.5")
               }
               {row_one_operation=="H":
                       ~ splitWorld(row_two_target)
               }

       }:
}
{row_two_control=="none":
               {row_two_operation=="X":
                       ~ degreeXGate(row_two_target,"0.5")
               }
               {row_two_operation=="Z":
                       ~ degreeZGate(row_two_target,"0.5")
               }
               {row_two_operation=="Y":
                       ~ degreeYGate(row_two_target,"0.5")
               }
               {row_one_operation=="H":
                       ~ splitWorld(row_two_target)
               }

}
}
Step 2 state is {left},{middle},{right}
{row_three_operation!="none":
{row_three_control=="left":
       {left==true:
               {row_three_operation=="X":
                       ~ degreeXGate(row_three_target,"0.5")
               }
               {row_three_operation=="Z":
                       ~ degreeZGate(row_three_target,"0.5")
               }
               {row_three_operation=="Y":
                       ~ degreeYGate(row_three_target,"0.5")
               }
               {row_three_operation=="H":
                       ~ splitWorld(row_three_target)
               }
       }:
}
{row_three_control=="middle":
       {middle==true:
               {row_three_operation=="X":
                       ~ degreeXGate(row_three_target,"0.5")
               }
               {row_three_operation=="Z":
                       ~ degreeZGate(row_three_target,"0.5")
               }
               {row_three_operation=="Y":
                       ~ degreeYGate(row_three_target,"0.5")
               }
               {row_three_operation=="H":
                       ~ splitWorld(row_three_target)
               }
       }:
}
{row_three_control=="right":
       {right==true:
               {row_three_operation=="X":
                       ~ degreeXGate(row_three_target,"0.5")
               }
               {row_three_operation=="Z":
                       ~ degreeZGate(row_three_target,"0.5")
               }
               {row_three_operation=="Y":
                       ~ degreeYGate(row_three_target,"0.5")
               }
               {row_one_operation=="H":
                       ~ splitWorld(row_three_target)
               }

       }:
}
{row_three_control=="none":
               {row_three_operation=="X":
                       ~ degreeXGate(row_three_target,"0.5")
               }
               {row_three_operation=="Z":
                       ~ degreeZGate(row_three_target,"0.5")
               }
               {row_three_operation=="Y":
                       ~ degreeYGate(row_three_target,"0.5")
               }
               {row_one_operation=="H":
                       ~ splitWorld(row_three_target)
               }

}
}
Finally the state is {left}, {middle}, {right}
->circuit