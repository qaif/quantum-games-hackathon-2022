using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using Ink.Runtime;
using TMPro;

public class test_ink_driver : MonoBehaviour
{

    [SerializeField]
    private TextAsset inkJSONAsset = null;
    public Story story;

    public TextMeshProUGUI text_shower;

    public int lines_happened;
    public double lineswitch_wait_ms;
    private double next_time_to_proceed;

    void Awake()
    {
        // Debug.Log("I am awake");
        // Remove the default message
        StartStory();
    }


    public static event Action<Story> OnCreateStory;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    void ThenThisHappens()
    {
        next_time_to_proceed = lines_happened * (lineswitch_wait_ms*(1.0/1000.0));
        Debug.Log(next_time_to_proceed.ToString()+ "lines "+ lines_happened.ToString());
        if (next_time_to_proceed < UnityEngine.Time.fixedTime)
        {
            if (story.canContinue)
            {
                string text = story.Continue();
                text_shower.SetText(text);
                Debug.Log(text);
                lines_happened = lines_happened + 1;
            }
            else
            {
                Debug.Log("story is stuck not continuing");
            }
        }
    }

    void StartStory()
    {
        story = new Story(inkJSONAsset.text);
        if (OnCreateStory != null) OnCreateStory(story);
        // Debug.Log("started");
        ThenThisHappens();
    }

    void FixedUpdate()
    {
        ThenThisHappens();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
