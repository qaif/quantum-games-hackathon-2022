    === auditorium ===
    The auditorium seems empty # narration
    ...except for a lone figure jumping up and down. #narration
    {sender_compartment==true:
          But you know the auditorium is not empty # narration
    }
    {sender_production==true:
           With the help of the student you uncover a big machine # narration
    }
    + [Engage]
        -> Rascal
    + {sender_compartment==true} Knock on wall panels
        ->TeleportSender
    + {sender_production==true} Examine big experiment machine
        ->TeleportProducer
    + Return to hallway
    -> hallway


=TeleportProducer
Yes it is a very complicated machine # narration
However the interface seems to be pretty simple # narration
There is just a one simple button # narration
produce new # written
{producer_plop:
   There is now a small box on the floor # narration
}
+ Press button
     ~ producer_plop=true
+ {producer_plop==true}Pick up small box
         {producer_carrying==true:
          In trying to reach a new cube you drop the old one. # narration
         -else:
          You pick up a cube. # narration
          ~producer_carrying=true
          ~producer_plop=false
         }
+ Leave
        {guilty=="rascal":
               {injury=="slice":
                          ~producer_plop=false
               }
        }
        ->auditorium
-
->TeleportProducer

=TeleportSender
Inside you find a weird device # narration
It indeed seem delicated and very fiddling inducing #narration
Please insert anti-correlation source # written
One part has that as instruction # narration
Please insert message # written
That one is a big hole in the side # narration
Engage season determination # written
Atleast found the big red button # narration
+ Insert item to anti-correlation source
      ~ com_sender_quantum_channel=true
+ Insert item to message slot
      {producer_carrying==true:
              well the superdyper password is something to try # narration
              ~ com_message_loaded=true
      }
+ Push red button
      {com_message_loaded==true:
         {com_sender_quantum_channel==true:
                   -> ComGeneration
         }
      }
+ Leave
    ->auditorium
-
->TeleportSender


=ComGeneration
{antisymmetry_alice==false:
    {com_state==false:
           ~com_delivery="spring"
    }
    {com_state==true:
           ~com_delivery="summer"
    }
}
{antisymmetry_alice==true:
    {com_state==false:
           ~com_delivery="fall"
    }
    {com_state==true:
           ~com_delivery="winter"
    }
}

Well the result seems to be {com_delivery} # narration

-> TeleportSender