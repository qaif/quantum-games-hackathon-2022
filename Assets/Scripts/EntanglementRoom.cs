using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EntanglementRoom : MonoBehaviour
{
    public QuantumState firstStateSet;
    public QuantumState secondStateSet;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

    }

    public void Entangle(List<(int, int)> mapping)
    {
        GameObject newParent = new GameObject();
        firstStateSet.transform.parent = newParent.transform;
        secondStateSet.transform.parent = newParent.transform;

        QuantumState newState = newParent.AddComponent<QuantumState>();
        newState.qubits.AddRange(firstStateSet.qubits);
        newState.qubits.AddRange(secondStateSet.qubits);

        foreach ((int a, int b) p in mapping)
        {
            QuantumState.State state = new QuantumState.State();
            state.state.AddRange(firstStateSet.superposition[p.a].state);
            state.state.AddRange(secondStateSet.superposition[p.b].state);
            state.colour = Random.Range(0, 2) == 0
                ? firstStateSet.superposition[p.a].colour
                : secondStateSet.superposition[p.b].colour;
            newState.superposition.Add(state);
        }
        newState.measurers.AddRange(firstStateSet.measurers);
        newState.measurers.AddRange(secondStateSet.measurers);

        foreach (Measurement measurer in newState.measurers)
        {
            measurer.stateToMeasure = newState;
        }
    }
}
