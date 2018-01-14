using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Gear : MonoBehaviour
{
    [SerializeField]
    private int numTooth = 12;

    [SerializeField]
    private List<GameObject> nextGearList = null;

    [SerializeField]
    private bool isConnectToNext = false;

    public void Rotate(float angle, int prevNumTooth)
    {
        this.Rotate(angle * prevNumTooth / this.numTooth);
    }

    public void Rotate(float angle)
    {
        transform.Rotate(0, angle, 0);
        this.RotateNextGear(angle);
    }

    private void RotateNextGear(float angle)
    {
        if (nextGearList == null)
        {
            return;
        }

        foreach (GameObject nextGear in this.nextGearList)
        {
            if (nextGear == null)
            {
                return;
            }

            Gear nextGearScript = nextGear.GetComponent<Gear>();
            if (nextGearScript == null)
            {
                return;
            }

            if (this.isConnectToNext)
            {
                nextGearScript.Rotate(angle);
            }
            else
            {
                nextGearScript.Rotate(-angle, this.numTooth);
            }
        }
    }
}

