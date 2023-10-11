using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class EntanglementPopup : MonoBehaviour
{
    public Image treeIcon;
    public float iconXSpacing = 25f;
    public float iconWidth = 50f;
    public float iconYOffset = 50f;

    public float lineWidth = 10f;

    public GameObject helpText;

    private EntanglementRoom lastRoom = null;
    private List<GameObject> treeIcons = new List<GameObject>();
    private List<(int, int, GameObject)> mapping = new List<(int, int, GameObject)>();

    enum Row
        {
            Top,
            Bottom
        }

    private Vector3? lineStart;
    private Row startRow;
    private int startIndex;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

    }

    GameObject DrawLine(Vector3 a, Vector3 b) {
        GameObject lineObject = new GameObject();
        lineObject.transform.parent = transform;
        Image lineImage = lineObject.AddComponent<Image>();
        lineImage.color = Color.white;
        RectTransform rect = lineObject.GetComponent<RectTransform>();
        rect.SetParent(transform);
        rect.localScale = Vector3.one;

        rect.localPosition = (a + b) / 2;
        Vector3 diff = a - b;
        rect.sizeDelta = new Vector3(diff.magnitude, lineWidth);
        rect.rotation = Quaternion.Euler(new Vector3(0, 0, 180 * Mathf.Atan(diff.y / diff.x) / Mathf.PI));

        return lineObject;
   }

    void DrawRowIcons(QuantumState stateSet, Row row)
    {
        int number = stateSet.superposition.Count;
        float currentXPos = - ((number - 1) * (iconWidth + iconXSpacing)) / 2f;

        for (int i = 0; i < number; i++)
        {
            GameObject treeIconObject = Instantiate(treeIcon.gameObject, transform);
            treeIcons.Add(treeIconObject);

            treeIconObject.transform.localPosition = new Vector3(currentXPos, row == Row.Top ? iconYOffset : -iconYOffset, 0f);

            Button button = treeIconObject.GetComponent<Button>();
            button.targetGraphic.color = stateSet.superposition[i].colour;
            int currentIndex = i;
            button.onClick.AddListener(() =>
            {
                helpText.gameObject.SetActive(false);
                if (lineStart == null || startRow == row)
                {
                    lineStart = treeIconObject.transform.localPosition;
                    startRow = row;
                    startIndex = currentIndex;
                }
                else if (startRow != row)
                {
                    (int top, int bottom) indices = startRow == Row.Top ? (startIndex, currentIndex) : (currentIndex, startIndex);
                    mapping = mapping.Where(((int top, int bottom, GameObject go) p) =>
                                            {
                                                if (p.top == indices.top || p.bottom == indices.bottom)
                                                {
                                                    Destroy(p.go);
                                                    return false;
                                                }
                                                return true;
                                            }).ToList();
                    GameObject line = DrawLine(lineStart.Value, treeIconObject.transform.localPosition);
                    mapping.Add((indices.top, indices.bottom, line));
                    lineStart = null;
                }
                return;
            });

            currentXPos += iconWidth + iconXSpacing;
        }
    }

    public void SetupPopup(EntanglementRoom room)
    {
        gameObject.SetActive(true);
        if (room == lastRoom)
        {
            return;
        }

        foreach (GameObject oldIcon in treeIcons)
        {
            Destroy(oldIcon);
        }
        treeIcons.Clear();
        lineStart = null;

        lastRoom = room;

        DrawRowIcons(room.firstStateSet, Row.Top);
        DrawRowIcons(room.secondStateSet, Row.Bottom);

    }

    public void ClosePopup()
    {
        helpText.gameObject.SetActive(false);
        gameObject.SetActive(false);
    }

    public void Entangle()
    {
        if (lastRoom == null)
            return;

        if (mapping.Count == lastRoom.firstStateSet.superposition.Count)
        {
            lastRoom.Entangle(mapping.Select(((int a, int b, GameObject go) m) => (m.a, m.b)).ToList());
            ClosePopup();
        }
        else
        {
            helpText.gameObject.SetActive(true);
        }
    }
}
