using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class QuantumState : MonoBehaviour
{
    [System.Serializable]
    public class State
    {
        public bool[] state;
        public Color colour;
    }

    public QTree[] qubits;
    public State[] superposition;

    // Start is called before the first frame update
    void Start()
    {
        foreach (State state in superposition)
        {
            for (int i = 0; i < qubits.Length; i++)
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
        int randomNum = Random.Range(0, superposition.Length);

        for (int i = 0; i < qubits.Length; i++)
        {
            qubits[i].Collapse(superposition[randomNum].state[i]);
        }

        gameObject.SetActive(false);
    }

}
