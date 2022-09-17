using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Ink.Runtime;

public class classical_story
{
    public Story story;

    private List<string> chronons;
    // Start is called before the first frame update
    void Start()
    {
        chronons = new List<string>();

    }

    public classical_story()
    {
        chronons = new List<string>();
    }

    public void force_add(string lol)
    {
        chronons.Add(lol);
    }


    void Awake()
    {
        chronons = new List<string>();
    }

    public string AsOneText()
    {
        string blob = "";
        for (int i = 0; i < chronons.Count; i++) 
        {
            blob = blob + "\n" + chronons[i];
        }
        if (story.currentChoices.Count > 0)
        {
            blob = blob + "\nHow shall I proceed?";
            for (int i = 0; i < story.currentChoices.Count; i++)
            {
                blob = blob + "\n" + story.currentChoices[i].text;
            }
        }
        return blob;
    }


    public void ForwardFlow()
    {
        while (story.canContinue)
        {
            string scribble = story.Continue();
            Debug.Log("chronon: "+ scribble);
            chronons.Add(scribble);
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
                chronons.Add(word+" doesn't make sense here");
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


    // Update is called once per frame
    void Update()
    {
        
    }
}
