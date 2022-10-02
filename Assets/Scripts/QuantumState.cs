using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class QuantumState : MonoBehaviour
{
    [System.Serializable]
    public class State
    {
        public List<bool> state = new List<bool>();
        public Color colour;
    }

    public List<QTree> qubits = new List<QTree>();
    public List<State> superposition = new List<State>();
    public List<Measurement> measurers = new List<Measurement>();

    // Start is called before the first frame update
    void Start()
    {
        foreach (State state in superposition)
        {
            for (int i = 0; i < qubits.Count; i++)
            {
                if (state.state[i])
                {
                    qubits[i].spriteRenderer.color = state.colour;
                }
            }
        }
    }

    // Update is called once per frame
    void Update()
    {

    }

    public void CollapseTrees()
    {
        int randomNum = Random.Range(0, superposition.Count);

        for (int i = 0; i < qubits.Count; i++)
        {
            qubits[i].Collapse(!superposition[randomNum].state[i]);
        }

        foreach (Measurement measurer in measurers)
        {
            measurer.gameObject.SetActive(false);
        }
    }

    public void ShowGlow()
    {
        foreach (QTree tree in qubits)
        {
            tree.glow.SetActive(true);
        }
    }

    public void HideGlow()
    {
        foreach (QTree tree in qubits)
        {
            tree.glow.SetActive(false);
        }
    }
}
