using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OriginGear : MonoBehaviour
{

    [SerializeField]
    private int numTooth = 15;

    [SerializeField]
    private GameObject nextGear = null;

    [SerializeField]
    private bool isConnectToNext = false;

    [SerializeField]
    private float timeTick = 0.4f;

    private bool isActive = true;
    private float timePrevious;

    void Start()
    {
        this.timePrevious = Time.realtimeSinceStartup;
    }

    void Update()
    {
        float timeNow = Time.realtimeSinceStartup;
        float timeSurplus = this.CalculateTimeSurplus(timeNow);
        float timeSurplusPrevious = this.CalculateTimeSurplus(this.timePrevious);
        float timeDelta = timeSurplus - timeSurplusPrevious + 0.000001f;
        if (timeDelta >= this.timeTick)
        {
            int tooth = (int)(timeDelta / this.timeTick);
            this.Rotate(-360f * tooth / this.numTooth);
            this.timePrevious = timeNow;
        }
    }

    private float CalculateTimeSurplus(float time)
    {
        return time - (time % this.timeTick);
    }

    public void Enable()
    {
        if (this.isActive)
        {
            return;
        }
        this.isActive = true;
    }

    public void Disable()
    {
        if (!this.isActive)
        {
            return;
        }
        this.isActive = false;
    }

    private void Rotate(float angle)
    {
        if (!this.isActive)
        {
            return;
        }
        transform.Rotate(0, angle, 0);
        RotateNextGear(angle);
    }

    private void RotateNextGear(float angle)
    {
        if (this.nextGear == null)
        {
            return;
        }

        Gear nextGearScript = this.nextGear.GetComponent<Gear>();
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
