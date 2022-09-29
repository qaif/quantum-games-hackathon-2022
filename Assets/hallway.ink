INCLUDE murder_bathroom.ink

=== hallway ===

The hallway seems empty. There is a door to the cleaning cellar, # narration
a door to a classroom, a wide opening to a cafeteria and a door to the auditorium. # narration
In addition to the usual facilities. # narration
~ clock=clock+1
The hall has a nice blue arc towards the outside with a mural depicting a lightly clouded sky. # narration
A nice green arc towards the inside has a mural of a grass field on it. # narration
{clock>5:
The middle arc is blue. Just boring solid color blue. # narration
-else:
The middle arc is green. Just boring solid color green. # narration
}
{clock>15:
     Hmmmm, there seems to be a smell around that grows stronger by the minute. # narration
}

{priority_note==true:
   Better get started with that toilet. # narration
}
    + {priority_note==false} Enter cleaning cellar
        -> cleaning_cellar.aEntersACleaning
    + {priority_note==false} Enter classroom
      -> classroom
    + {priority_note==false} Enter auditorium
        ->auditorium 
    + {priority_note==false} Enter office
        ->office
    + {priority_note==false} Enter post station
        -> CatDelivery
    + Usual facilities
        -> Facilities

=Facilities
    {guilty=="merry":
    That is funny. I thought I cleaned up this end of the hallway yesterday. # narration
    }
    + Enter toilet
        ->MurderBathroom
    + {priority_note==false} Enter hall of fame
       -> HallOfFame
    + {priority_note==false} Enter cafeteria
       -> Coffee.coffeetable
    + Unusual facilities
       -> hallway
    
    
    
    
    === classroom ===
    The classroom seems echoing, but there is someone behind a high bookstack. # narration
    + [Engage]
        -> Runa_cat
    + Return to hallway
    -> hallway
    
    === auditorium ===
    The auditorium seems empty # narration
    ...except for a lone figure jumping up and down. #narration
    {sender_compartment==true:
          But you know the auditorium is not empty # narration
    }
    {teleport_production==true:
           With the help of the student you uncover a big machine # narration
    }
    + [Engage]
        -> Rascal
    + {sender_compartment==true} Knock on wall panels
        ->TeleportSender
    + {teleport_production==true} Examine big experiment machine
        ->TeleportProducer
    + Return to hallway
    -> hallway


=TeleportProducer
Yes it is a very compicated machine # narration
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
      com_sender_quantum_channel=true
+ Insert item to message slot
      {producer_carrying==true:
              well the superdyper password is something to try
              ~ com_message_loaded=true
      }
+ Push red button
      {com_message_loaded==true:
         {com_sender_quantum_channel==true:
                   -> ComGeneration
         }
      }
+ Leave
-
->TeleportSender


=ComGeneration
{antisymmetry_alice==false:
    {com_state==false:
           ~com_delivery="spring";
    }
    {com_state==true:
           ~com_delivery="summer";
    }
}
{antisymmetry_alice==true:
    {com_state==false:
           ~com_delivery="fall";
    }
    {com_state==true:
           ~com_delivery="winter";
    }
}

Well the result seems to be {com_delivery} # narration

-> TeleportSender