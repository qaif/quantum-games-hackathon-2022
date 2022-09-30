using System.Collections;
using System.Collections.Generic;
using System.Numerics;
using UnityEngine;
using Ink.Runtime;

public class classical_story
{
    public Story story;

    public event_chain past;
    public bool the_end_is_here;
    public superposition_manager quantumLord;
    private char[] numeral_glyphs;
    private List<string> socials;
    public TextAsset manuscript;
    public string bifurcateFlag;
    public double bifurcateDegree;
    public Complex realityFluid;
    public int newSection;
    public int oldAmount;
    // Start is called before the first frame update


    public classical_story(superposition_manager lord,TextAsset script)
    {
        manuscript = script;
        story = new Story(script.text);
        past = new event_chain();
        socials = new List<string>();
        the_end_is_here = false;
        quantumLord = lord;
        bifurcateFlag = "";
        newSection = 0;
        oldAmount = 0;
        realityFluid = new Complex(1.0, 0.0);
        numeral_glyphs = new char[] { '0','1', '2', '3', '4', '5', '6', '7', '8', '9' };
    }

    /*
    public void force_add(string lol)
    {
        chronons.Add(new Chronon(lol,new string[] { "forced"}));
    }*/

    public string AsOneText()
    {
        string blob = "";
        foreach (Chronon bloblet in past.DisplayChronons(0.0)) 
        {
            blob = blob + "\n" + bloblet.prose;
        }
        if (story.currentChoices.Count > 0)
        {
            blob = blob + "\nHow shall I proceed?";
            for (int i = 0; i < story.currentChoices.Count; i++)
            {
                blob = blob + "\n" + (i+1).ToString()+") "+ story.currentChoices[i].text;
            }
        }
        return blob;
    }


    public void ForwardFlow()
    {
        while (story.canContinue)
        {
            if (bifurcateFlag == "")
            {
                string scribble = story.Continue();
                //Debug.Log("chronon: "+ scribble);
                socials = new List<string>();
                past.Add(new Chronon(scribble, story.currentTags.ToArray()));
            }
            else
            {
                return;
            }
        }
        if (story.currentChoices.Count <= 0)
        {
            the_end_is_here = true;
        }
    }

    public List<Chronon> DisplayChronons(double clockhand)
    {
        List<Chronon> basket = past.DisplayChronons(clockhand);
        basket.Insert(basket.Count-newSection,new Chronon("----------------------",new string[] { "program" }));
        return basket;
    }

    public double NextChange(double clockhand)
    {
        return past.NextChange(clockhand)*realityFluid.Magnitude;
    }

    public List<Chronon> affordanceItems()
    {
        List<Chronon> basket = new List<Chronon>();
        if (story.currentChoices.Count > 0)
        {
            for (int i=0; i < story.currentChoices.Count; i++)
            {
                basket.Add(new Chronon(story.currentChoices[i].text,story.currentTags.ToArray()));
            }
        }
        return basket;
    }

    public void phaseGate(string detail, double degree=0.5)
    {
        if (story.variablesState[detail].ToString() == "True")
        {
            realityFluid = realityFluid * Complex.FromPolarCoordinates(1.0, (degree * System.Math.PI * 2));
        }
    }
    public void flipGate(string detail, double degree=0.5)
    {
        if (story.variablesState[detail].ToString() == "True")
        {
            story.variablesState[detail] = false;
        }
        else
        {
            story.variablesState[detail] = false;
        }
    }
    public void crossGate(string detail, double degree=0.5)
    {
        if (story.variablesState[detail].ToString() == "True")
        {
            story.variablesState[detail] = false;
            realityFluid = realityFluid * Complex.FromPolarCoordinates(1.0, (System.Math.PI / 2.0));
        }
        else
        {
            story.variablesState[detail] = false;
            realityFluid = realityFluid * Complex.FromPolarCoordinates(1.0, (System.Math.PI * 1.5));
        }
    }

    public void bifurcate(classical_story reference)
    {
        //Debug.Log("Top feeder");
        //Debug.Log("Bottom feeder");
        //string old_content = story.ToJson();
        //string old_state = story.state.ToJson();

        //Debug.Log(old_content);
        //Debug.Log(noob.story.variablesState[detail]);


        string old_content = reference.story.state.ToJson();
        story.state.LoadJson(old_content);

        /*  tricky manual way of saving - past advices against using
        while (story.canContinue)
        {
            Debug.Log(story.Continue());
        }
        foreach(string individual in quantumLord.copied_variables)
        {
            Debug.Log("insider");
            story.variablesState[individual] = reference.story.variablesState[individual];
        }
        story.variablesState["warp_story"] = "true";
        story.variablesState["warp_target"] = warppoint;

        //Debug.Log(noob.story.Continue());
        Debug.Log("Toggle point before: " + story.variablesState[detail].ToString());
        */
        Debug.Log(bifurcateFlag.ToString());
        //Debug.Log(story.variablesState[bifurcateFlag].ToString());

        //realityFluid = reference.realityFluid;
        Debug.Log("nooob prestate "+story.variablesState[bifurcateFlag].ToString()+ story.variablesState["world"]);

        if (story.variablesState[bifurcateFlag].ToString() == "True")
        {
            //Debug.Log("activated?");
            story.variablesState[bifurcateFlag] = false; // wonder if right format
            //realityFluid = realityFluid * (-1.0); This is wrong, crossline from right to left in hadamar. Hadamar has only one red edge on the right straight down
        }
        else
        {
            story.variablesState[bifurcateFlag] = true; // left to right diagonal on hadamar
        }
        Debug.Log("nooob after state"+story.variablesState[bifurcateFlag].ToString() + story.variablesState["world"]);
        past = new event_chain(reference.past.splitCopy());
        /*
        Debug.Log("CHOICE:"+story.currentChoices.Count.ToString());
        story.ChooseChoiceIndex(0);
        story.Continue();
        ForwardFlow();
        story.variablesState["warp_story"] = false;
        story.variablesState["warp_target"] = "";
        */
    }

    public double thickness()
    {
        return past.thickness*realityFluid.Magnitude;
    }

    public void renormalize(double rate)
    {
        past.renormalize(rate);
    }

    public double minimum_point_thickness()
    {
        return past.minimum_point_thickness()*realityFluid.Magnitude;
    }

    public void HeedAction(string word)
    {
        if (story.currentChoices.Count > 0)
        {
            for (int i = 0; i < story.currentChoices.Count; i++)
            {
                Choice choice = story.currentChoices[i];
                if (choice.text.ToLower() == word.ToLower())
                {
                    story.ChooseChoiceIndex(i);
                }
            }
            if (!story.canContinue)
            {
                if (word.Length > 0)
                {
                    int numerals = 0;
                    int i = 0;
                    string text_number = "";
                    while (System.Array.Exists(numeral_glyphs, x => x == word[i]))
                    {
                        text_number = text_number + word[i].ToString();
                        numerals = numerals + 1;
                        i++;
                        if (i >= word.Length)
                        {
                            break;
                        }
                    }
                    if (text_number.Length > 0)
                    {
                        int choice_index = System.Int32.Parse(text_number)-1;
                        if (choice_index < 0)
                        {
                            past.Add(new Chronon("You do nothing. No operation. NOP",new string[] { "program"}));
                        }
                        else
                        {
                            if (choice_index <= story.currentChoices.Count)
                            {
                                story.ChooseChoiceIndex(choice_index);
                                ForwardFlow();
                            }
                            else
                            {
                                if (text_number == "2845")
                                {
                                    story.variablesState["keypad"] = true;
                                }
                                else
                                {
                                    past.Add( new Chronon("You have run out of pages in your playbook to try that trick.",new string[] { "program"}) );
                                }
                            }
                        }
                    }
                    else
                    {
                        past.Add( new Chronon(word + " doesn't make sense here",new string[] { "program"}) );
                    }
                }
                else
                {
                    past.Add( new Chronon("Well this time Time insists and waits for you to do something.", new string[] { "program"}) );
                }
            }
            else
            {
                ForwardFlow();
            }
        }
        else
        {
            Debug.Log("classical story stuck in non-choice");
        }
        int depth = past.CountMax();
        newSection = depth - oldAmount;
        oldAmount = depth;

    }

    public string CoherentLottery(string lottery_type)
    {
        return quantumLord.CoherentLottery(this, lottery_type);
    }


    // Update is called once per frame
    void Update()
    {
        
    }
}
