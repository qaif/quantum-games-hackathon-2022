using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Ink.Runtime;

public class classical_story
{
    public Story story;

    private List<Chronon> chronons;
    public bool the_end_is_here;
    public superposition_manager quantumLord;
    private char[] numeral_glyphs;
    private List<string> socials;
    // Start is called before the first frame update

    public classical_story(superposition_manager lord,TextAsset script)
    {
        story = new Story(script.text);
        chronons = new List<Chronon>();
        socials = new List<string>();
        the_end_is_here = false;
        quantumLord = lord;
        numeral_glyphs = new char[] { '0','1', '2', '3', '4', '5', '6', '7', '8', '9' };
    }

    public void force_add(string lol)
    {
        chronons.Add(new Chronon(lol,new string[] { "forced"}));
    }

    public string AsOneText()
    {
        string blob = "";
        for (int i = 0; i < chronons.Count; i++) 
        {
            blob = blob + "\n" + chronons[i].prose;
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
            string scribble = story.Continue();
            //Debug.Log("chronon: "+ scribble);
            socials = new List<string>();
            chronons.Add(new Chronon(scribble,story.currentTags.ToArray()));
        }
        if (story.currentChoices.Count <= 0)
        {
            the_end_is_here = true;
        }
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
                            chronons.Add(new Chronon("You do nothing. No operation. NOP",new string[] { "program"}));
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
                                    chronons.Add( new Chronon("You have run out of pages in your playbook to try that trick.",new string[] { "program"}) );
                                }
                            }
                        }
                    }
                    else
                    {
                        chronons.Add( new Chronon(word + " doesn't make sense here",new string[] { "program"}) );
                    }
                }
                else
                {
                    chronons.Add( new Chronon("Well this time Time insists and waits for you to do something.", new string[] { "program"}) );
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
