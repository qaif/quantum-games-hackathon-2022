using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Ink.Runtime;
using TMPro;
using System.Numerics;

public class superposition_manager : MonoBehaviour
{
    public TextAsset line_template;
    public List<classical_story> linears;
    public TMP_InputField commander;
    public int current_display;
    public TextMeshProUGUI current_prose;
    public TextMeshProUGUI current_prose_2;
    public TextMeshProUGUI current_prose_3;
    public TextMeshProUGUI current_prose_4;
    public TextMeshProUGUI current_prose_5;
    public List<GameObject> display_grids;
    public double time_to_keep_stable;
    private double last_rollover;
    private List<string> world_letters;

    public TextMeshProUGUI ProgramSlateFactory;
    public TextMeshProUGUI ProtagonistSlateFactory;
    public TextMeshProUGUI NarrationSlateFactory;
    public TextMeshProUGUI RascalSlateFactory;

    public Canvas paint_wall;

    public string[] copied_variables;

    public Dictionary<string, Lottery> lotto;

    public Dictionary<classical_story,classical_story> AddQuota;
    public List<classical_story> annhilationQueue;
    public List<classical_story> removeQueue;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    void Awake()
    {
        copied_variables = new string[] { "world" ,"injury","storm","werewolf","guilty","weapon","protagonist_name","debt","affair","critter","priority_note","lucan_potion","lucan_extort","lucan_cure","lucan_borrow","lucan_identity","lucan_formula","lucan_points","post_task","post_revenge","post_box_label","post_cat_up","post_cat_dead","post_neurotoxin","post_bomb_armed","post_bomb_exploded","post_probe","post_china","post_bomb_error","post_bomb_burden","passcode"};
        AddQuota = new Dictionary<classical_story, classical_story>();
        annhilationQueue = new List<classical_story>();
        removeQueue = new List<classical_story>();
        current_display = 0;
        last_rollover = 0.0;
        world_letters = new List<string>();
        world_letters.Add("A");
        world_letters.Add("B");
        world_letters.Add("C");
        world_letters.Add("D");
        world_letters.Add("E");
        display_grids = new List<GameObject>();
        FromTheTop();

    }

    void HeedAction(string word)
    {
        //Debug.Log("start heed");
        foreach (classical_story line in linears)
        {
            //Debug.Log("linear");
            line.HeedAction(word);
        }
        forkment();
        Admissions();
        annhilations();
        RefreshDisplays();
        commander.ActivateInputField();
    }

    void Admissions()
    {

        List<classical_story> rollers = new List<classical_story>();
        foreach(KeyValuePair<classical_story,classical_story> huikka in AddQuota)
        {
            int paikka = linears.IndexOf(huikka.Key);
            linears.Insert(paikka, huikka.Value);
            rollers.Add(huikka.Value);
        }
        //Debug.Log("LC" + linears.Count.ToString());
        AddQuota = new Dictionary<classical_story, classical_story>();
        foreach (classical_story noob in rollers)
        {
            //Debug.Log(noob.story.currentText);
            noob.ForwardFlow();          
        }
        forkment();
        if (AddQuota.Count > 0)
        {
            Admissions();
        }
    }

    void ShowNext()
    {
        current_display = current_display + 1;
        if (current_display >= linears.Count)
        {
            current_display = 0;
            last_rollover = Time.time;
        }
        int limit = 0;
        while (linears[current_display].the_end_is_here == true && limit<100) {
            current_display = current_display + 1;
            if (current_display >= linears.Count)
            {
                current_display = 0;
                last_rollover = Time.time;
            }
            limit = limit + 1;
        }
        if (limit >= 100)
        {
            EndShow();
        }
        current_prose.SetText("");
        RefreshDisplays();


    }

    void EndShow()
    {
        bool retry_ask = false;
        for (int i=0; i<linears.Count; i++)
        {
            if (linears[i].story.variablesState["retry"].ToString() == "true")
            {
                retry_ask = true;
            }
        }
        commander.onSubmit.RemoveListener(HeedAction);
        if (retry_ask)
        {
            FromTheTop();
        }
        else
        {
            Application.Quit();
            Debug.Log("THE GAME EXITED");
        }
    }

    void FromTheTop()
    {
        lotto = new Dictionary<string, Lottery>();
        string[] dual = new string[] { "true","false"};
        Lottery a = new Lottery(dual);
        //Debug.Log(dual);
        Lottery b = new Lottery(dual);
        Lottery c = new Lottery(new string[]{"animal","handle with care","express"});
        lotto.Add("atomic_fact",a);
        lotto.Add("bomb_fuse",b);
        lotto.Add("box_label", c);

        linears = new List<classical_story>();
        for (int i = 0; i < 5; i++)
        {

            classical_story fresh = new classical_story(this,line_template);
            //fresh.force_add("story "+i.ToString());
            fresh.story.onError += (huuto, what) =>
            {
                catchError(world_letters[i], huuto, what);
            };
            superposition_manager echo_copy = this;
            int j = i;
            fresh.story.BindExternalFunction("coherentLottery", (string ticket) => {
                string midway = echo_copy.CoherentLottery(fresh, ticket);
                return midway;
            });
            classical_story noblet = fresh;
            fresh.story.BindExternalFunction("splitWorld", (string corner) =>
            {
                //Debug.Log("boo");
                splitWorld(noblet, corner);
            });

            fresh.ForwardFlow();
            fresh.story.variablesState["world"] = world_letters[i];
            linears.Add(fresh);
            //Debug.Log("plop");

        }
        //HeedAction("test");
        commander.onSubmit.AddListener(HeedAction);
        RefreshDisplays();
        commander.ActivateInputField();
    }


    void RefreshDisplays()
    {
        for (int i=0; i < display_grids.Count; i++)
        {
            GameObject.Destroy(display_grids[i]);
        }
        display_grids = new List<GameObject>();
        float vertical_spacing=0.3f;
        float height_start = (linears[current_display].chronons.Count*vertical_spacing)-3.0f;
        for (int i=0; i < linears[current_display].chronons.Count; i++)
        {
            TextMeshProUGUI noob = null;
            if (System.Array.Exists(linears[current_display].chronons[i].notes, x => x == "protagonist"))
            {
                noob=Instantiate(ProtagonistSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            if (System.Array.Exists(linears[current_display].chronons[i].notes, x => x == "narration"))
            {
                noob=Instantiate(NarrationSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            if (System.Array.Exists(linears[current_display].chronons[i].notes, x => x == "program"))
            {
                noob=Instantiate(ProgramSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            if (System.Array.Exists(linears[current_display].chronons[i].notes, x => x == "rascal"))
            {
                noob = Instantiate(RascalSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            if (noob == null)
            {
                noob=Instantiate(ProgramSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            noob.SetText(linears[current_display].chronons[i].prose);
            noob.transform.SetParent(paint_wall.transform,true);
            noob.transform.localScale = new UnityEngine.Vector3(1.0f,1.0f,1.0f);
            display_grids.Add(noob.gameObject);
        }
        List<Chronon> affords = linears[current_display].affordanceItems();
        float horizontal_start = 3.0f;
        vertical_spacing = 0.2f;
        height_start = (affords.Count * vertical_spacing) - 4.0f;
        for (int i=0; i < affords.Count; i++)
        {
            TextMeshProUGUI noob = null;
            /*if (System.Array.Exists(affords[i].notes, x => x == "protagonist"))
            {
                noob = Instantiate(ProtagonistSlateFactory, new Vector3(horizontal_start, height_start - (i * vertical_spacing), 0), Quaternion.identity);
            }
            if (System.Array.Exists(affords[i].notes, x => x == "narration"))
            {
                noob = Instantiate(NarrationSlateFactory, new Vector3(horizontal_start, height_start - (i * vertical_spacing), 0), Quaternion.identity);
            }
            if (System.Array.Exists(affords[i].notes, x => x == "program"))
            {
                noob = Instantiate(ProgramSlateFactory, new Vector3(horizontal_start, height_start - (i * vertical_spacing), 0), Quaternion.identity);
            }
            */
            if (noob == null)
            {
                noob = Instantiate(ProgramSlateFactory, new UnityEngine.Vector3(horizontal_start, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            noob.SetText((i+1).ToString()+") "+affords[i].prose);
            noob.transform.SetParent(paint_wall.transform, true);
            noob.transform.localScale = new UnityEngine.Vector3(1.0f, 1.0f, 1.0f);
            display_grids.Add(noob.gameObject);

        }


        string payload = linears[current_display].AsOneText();
        current_prose.SetText(payload);
        current_prose_2.SetText(payload);
        current_prose_3.SetText(payload);
        current_prose_4.SetText(payload);
        current_prose_5.SetText(payload);
    }

    void catchError(string storyid,string huuto, Ink.ErrorType what)
    {
        Debug.Log("story "+storyid+" "+what.ToString() + " : " + huuto);
    }

    public void forkment()
    {
        foreach (classical_story focus in linears)
        {
            if (focus.bifurcateFlag != "")
            {
                classical_story noob = new classical_story(this, focus.manuscript);
                noob.bifurcateFlag = focus.bifurcateFlag;
                focus.realityFluid = focus.realityFluid / 2.0;
                noob.bifurcate(focus);
                foreach (KeyValuePair<string, Lottery> finger in lotto)
                {
                    finger.Value.dupe(focus, noob);
                }
                //Debug.Log("even deeper");
                noob.story.BindExternalFunction("coherentLottery", (string ticket) =>
                {
                    string midway = CoherentLottery(noob, ticket);
                    return midway;
                });
                noob.story.BindExternalFunction("splitWorld", (string corner) =>
                {
                    splitWorld(noob, corner);
                });
                noob.bifurcateFlag = "";
                focus.bifurcateFlag = "";
                AddQuota.Add(focus, noob);
                annhilationQueue.Add(noob);
                focus.ForwardFlow();
            }
        }
    }


    public void splitWorld(classical_story river, string detail)
    {
        river.bifurcateFlag = detail;
    }

    public void annhilations()
    {
        /*
        Debug.Log("Sanity test start");
        if (annhilationQueue.Count>0)
        {
            foreach (string huh in annhilationQueue[0].story.variablesState)
            {
                Debug.Log(huh);
            }
        }*/
        int aggressors = 0;
        int defenders = 0;
        int crossref = 0;
        int crosstotal = 0;
        int drops = 0;
        List<string> defbasket = new List<string>();
        foreach (classical_story aggressor in annhilationQueue)
        {
            aggressors += 1;
            defenders = 0;
            crossref = 0;
            foreach (classical_story defender in linears)
            {
                defenders += 1;
                if (aggressor != defender)
                {
                    bool defender_dodge = false;
                    foreach (string atkdetail in aggressor.story.variablesState)
                    {
                        //Debug.Log(atkdetail);
                        if (!(defender.story.variablesState[atkdetail].Equals(aggressor.story.variablesState[atkdetail])))
                        {
                            //Debug.Log("CLASH " + atkdetail);
                            defender_dodge = true;
                            break;
                        }
                    }
                    if (defender_dodge)
                    {
                        continue;
                    }
                    else
                    {
                        double before_reference = defender.realityFluid.Magnitude + aggressor.realityFluid.Magnitude;
                        Complex before_amount = defender.realityFluid;
                        defender.realityFluid = defender.realityFluid + aggressor.realityFluid;
                        double diff = defender.realityFluid.Magnitude - before_reference;
                        drops += 1;
                        Debug.Log("BOOOM " + before_reference.ToString() +"BC: "+ before_amount.ToString()+ " A: " + aggressor.realityFluid.ToString()+ " C: " + defender.realityFluid.ToString()+ "Diff:" +diff.ToString());
                        removeQueue.Add(aggressor);
                        if (defender.realityFluid.Magnitude < 0.00001)
                        {
                            Debug.Log("fallen defender" + defender.realityFluid.ToString());
                            removeQueue.Add(defender);
                        }
                        if (current_display > defenders)
                        {
                            current_display -= 1;
                        }
                    }
                }
            }
            crosstotal += crossref;
        }
        Debug.Log("Annhilation ags:" + aggressors.ToString() + "defs: " + defenders.ToString() +"booms:"+drops.ToString()+ "crossreftotal: " + crosstotal.ToString());
        annhilationQueue = new List<classical_story>();
        foreach(classical_story convict in removeQueue)
        {
            linears.Remove(convict);
        }
        removeQueue = new List<classical_story>();
        Debug.Log("annhilation done"+linears.Count);
    }


    public string CoherentLottery(classical_story river,string lotterytype)
    {
        for (int i=0; i < linears.Count; i++)
        {
            if (linears[i] == river)
            {
                string result= lotto[lotterytype].provide(linears[i]);
                Debug.Log(result + " " + i);
                return result;
            }
        }
        Debug.Log("failed to identify lottery");
        return "The player is not supposed to see this";
    }


    // Update is called once per frame
    void Update()
    {
        double time_phase = Time.time - last_rollover;
        //Debug.Log(time_phase+ (time_to_keep_stable * (current_display+1)).ToString());
        if (time_phase > (time_to_keep_stable * (current_display+1)))
        {
            //Debug.Log("whoosh");
            ShowNext();
        }
    }
}
