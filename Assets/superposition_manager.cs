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
    public double current_display;
    public TextMeshProUGUI current_prose;
    public TextMeshProUGUI current_prose_2;
    public TextMeshProUGUI current_prose_3;
    public TextMeshProUGUI current_prose_4;
    public TextMeshProUGUI current_prose_5;
    public List<GameObject> display_grids;
    public double time_to_keep_stable;
    public double full_cycle_time;
    private double last_rollover;
    private double coming_nudgement;
    private double inflation;
    private double timeToSpend;
    private List<string> world_letters;

    int linear_track;

    public TextMeshProUGUI ProgramSlateFactory;
    public TextMeshProUGUI ProtagonistSlateFactory;
    public TextMeshProUGUI NarrationSlateFactory;
    public TextMeshProUGUI RascalSlateFactory;
    public TextMeshProUGUI HandwriteSlateFactory;
    public TextMeshProUGUI ButlerSlateFactory;
    public TextMeshProUGUI MathTSlateFactory;
    public TextMeshProUGUI ChemistryTSlateFactory;
    public TextMeshProUGUI HistoryTSlateFactory;
    public TextMeshProUGUI RunaSlateFactory;

    public Canvas paint_wall;

    public string[] copied_variables;

    public Dictionary<string, Lottery> lotto;

    public Dictionary<classical_story,classical_story> AddQuota;
    public List<classical_story> annhilationQueue;
    public List<classical_story> removeQueue;

    public classical_story current_linear;
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
        current_display = 0.0;
        coming_nudgement = 0.0;
        last_rollover = 0.0;
        inflation = 0.0;
        timeToSpend =full_cycle_time;
        linear_track = 0;
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

    /*
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
    */

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
            fresh.story.BindExternalFunction("degreeSplitWorld", (string corner, string amount) =>
            {
                Debug.Log("incoming " + amount);
                splitWorld( fresh, corner, double.Parse(amount,System.Globalization.CultureInfo.InvariantCulture) );
            });


            fresh.ForwardFlow();
            fresh.story.variablesState["world"] = world_letters[i];
            fresh.past.thickness = 20.0;
            linears.Add(fresh);
            //Debug.Log("plop");

        }
        //HeedAction("test");
        current_linear = linears[0];
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
        if (inflation < 0.0001)
        {
            inflation = 1.0;
        }
        List<Chronon> bask_subjects = DisplayChronons(current_display);
        float height_start = (bask_subjects.Count*vertical_spacing)-3.0f;
        for (int i=0; i < bask_subjects.Count; i++)
        {
            TextMeshProUGUI noob = null;
            if (System.Array.Exists(bask_subjects[i].notes, x => x == "protagonist"))
            {
                noob=Instantiate(ProtagonistSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            if (System.Array.Exists(bask_subjects[i].notes, x => x == "narration"))
            {
                noob=Instantiate(NarrationSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            if (System.Array.Exists(bask_subjects[i].notes, x => x == "program"))
            {
                noob=Instantiate(ProgramSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            if (System.Array.Exists(bask_subjects[i].notes, x => x == "rascal"))
            {
                noob = Instantiate(RascalSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            if (System.Array.Exists(bask_subjects[i].notes, x => x == "handwritten"))
            {
                noob = Instantiate(HandwriteSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            if (System.Array.Exists(bask_subjects[i].notes, x => x == "butler"))
            {
                noob = Instantiate(ButlerSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            if (System.Array.Exists(bask_subjects[i].notes, x => x == "mathT"))
            {
                noob = Instantiate(MathTSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            if (System.Array.Exists(bask_subjects[i].notes, x => x == "chemistryT"))
            {
                noob = Instantiate(ChemistryTSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            if (System.Array.Exists(bask_subjects[i].notes, x => x == "historyT"))
            {
                noob = Instantiate(HistoryTSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            if (System.Array.Exists(bask_subjects[i].notes, x => x == "runa"))
            {
                noob = Instantiate(RunaSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            if (noob == null)
            {
                noob=Instantiate(ProgramSlateFactory, new UnityEngine.Vector3(0, height_start - (i * vertical_spacing), 0), UnityEngine.Quaternion.identity);
            }
            noob.SetText(bask_subjects[i].prose);
            noob.transform.SetParent(paint_wall.transform,true);
            noob.transform.localScale = new UnityEngine.Vector3(1.0f,1.0f,1.0f);
            display_grids.Add(noob.gameObject);
        }
        List<Chronon> affords = current_linear.affordanceItems();
        float horizontal_start = 5.0f;
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


        string payload = current_linear.AsOneText();
        current_prose.SetText(payload);
        current_prose_2.SetText(payload);
        current_prose_3.SetText(payload);
        current_prose_4.SetText(payload);
        current_prose_5.SetText(payload);
    }

    void catchError(string storyid,string huuto, Ink.ErrorType what)
    {
        Debug.Log("story ERROR "+storyid+" "+what.ToString() + " : " + huuto);
    }

    public List<Chronon> DisplayChronons(double clockhand)
    {
        double time_offset = clockhand;
        foreach (classical_story river in linears)
        {
            double span = river.thickness();
            if (time_offset < span)
            {
                current_linear = river;
                return river.DisplayChronons(time_offset);
            }
            time_offset -= span;
        }
        Debug.Log("forbidden area DC "+clockhand.ToString());
        return new List<Chronon>();
    }

    public double NextChange(double clockhand)
    {
        double time_offset = clockhand;
        double creep = 0.0;
        foreach (classical_story river in linears)
        {
            double span = river.thickness();
            if (time_offset < span)
            {
                return creep+river.NextChange(time_offset);
            }
            creep += span;
            time_offset -= span;
        }
        Debug.Log("forbidden area");
        return creep + time_offset;

    }

    public void forkment()
    {
        foreach (classical_story focus in linears)
        {
            if (focus.bifurcateFlag != "")
            {
                classical_story noob = new classical_story(this, focus.manuscript);
                noob.bifurcateFlag = focus.bifurcateFlag;
                noob.realityFluid = focus.realityFluid * focus.bifurcateDegree;
                focus.realityFluid = focus.realityFluid * (1.0-focus.bifurcateDegree);
                focus.renormalize(1.0-focus.bifurcateDegree);
                noob.bifurcate(focus);
                noob.renormalize(focus.bifurcateDegree);
                Debug.Log("focus prestate"+ focus.story.variablesState[focus.bifurcateFlag].ToString() + focus.story.variablesState["world"]);
                foreach (KeyValuePair<string, Lottery> finger in lotto)
                {
                    finger.Value.dupe(focus, noob);
                }

                if (focus.story.variablesState[focus.bifurcateFlag] .ToString()== "True") // right straight down hadamar
                {
                    focus.realityFluid = focus.realityFluid * (-1.0);
                }
                else
                {
                    // left straight down hadamar
                }

                Debug.Log("focus afterstate" + focus.story.variablesState[focus.bifurcateFlag].ToString() + focus.story.variablesState["world"]);

                //Debug.Log("even deeper");
                //fresh.force_add("story "+i.ToString());
                noob.story.onError += (huuto, what) =>
                {
                    catchError("splitted", huuto, what);
                };
                noob.story.BindExternalFunction("coherentLottery", (string ticket) =>
                {
                    string midway = CoherentLottery(noob, ticket);
                    return midway;
                });
                noob.story.BindExternalFunction("splitWorld", (string corner) =>
                {
                    splitWorld(noob, corner);
                });
                noob.story.BindExternalFunction("degreeSplitWorld", (string corner,string amount) =>
                {
                    splitWorld(noob, corner,double.Parse(amount, System.Globalization.CultureInfo.InvariantCulture));
                });
                noob.bifurcateFlag = "";
                focus.bifurcateFlag = "";
                AddQuota.Add(focus, noob);
                annhilationQueue.Add(noob);
                focus.ForwardFlow();
            }
        }
    }


    public void splitWorld(classical_story river, string detail, double degree=0.5)
    {
        Debug.Log("flagger "+detail);
        river.bifurcateFlag = detail;
        river.bifurcateDegree = degree;
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
                        defender.past = new event_chain(defender.past.splitCopy(),aggressor.past.splitCopy());
                        Debug.Log("annhilation fat"+ defender.past.thickness.ToString());
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
        double fat = 0;
        double min_thickness = float.MaxValue;
        foreach(classical_story river in linears)
        {
            fat += river.thickness();
            double rapids = river.minimum_point_thickness();
            if (rapids < min_thickness)
            {
                min_thickness = rapids;
            }
            //Debug.Log("fatreport" + river.thickness().ToString());
        }
        double cut_factor = 1.0 / fat;
        foreach (classical_story river in linears)
        {
            river.renormalize(cut_factor);
        }
        if (time_phase > timeToSpend)
        {
            last_rollover += timeToSpend;
            current_display = 0.0;
            RefreshDisplays();
            coming_nudgement = NextChange(0.0);
            //Debug.Log("whoosh");
            //ShowNext();
        }
        else
        {
            timeToSpend =full_cycle_time;
            double progress = time_phase / timeToSpend;
            if (linear_track != linears.Count)
            {
                linear_track = linears.Count;
                Debug.Log(progress.ToString() + "  " + min_thickness.ToString() + "fat" + fat.ToString() + " entities " + linears.Count.ToString());
            }
            current_display = progress;
            if (current_display > coming_nudgement)
            {
                RefreshDisplays();
                coming_nudgement=NextChange(current_display);
                Debug.Log("Next post "+coming_nudgement.ToString());
            }
            //Debug.Log(linears.Count);
            //Debug.Log("timing " + progress.ToString() + " span " + current_display.ToString() + " coming " + coming_nudgement.ToString());
        }
    }
}
