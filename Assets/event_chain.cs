using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class event_chain
{
    public List<Chronon> linear_bit;
    public event_chain trunk_branch;
    public event_chain leaf_branch;
    public double thickness;

    public event_chain(event_chain trunk = null, event_chain leaf = null)
    {
        linear_bit = new List<Chronon>();
        thickness = 0.0;
        trunk_branch = trunk;
        leaf_branch = leaf;
        if (trunk_branch != null)
        {
            thickness += trunk_branch.thickness;
        }
        if (leaf_branch != null)
        {
            thickness += trunk_branch.thickness;
        }
    }

    public event_chain splitCopy()
    {
        event_chain leaf_copy = null;
        event_chain trunk_copy = null;
        if (trunk_branch != null)
        {
            trunk_copy = trunk_branch.splitCopy();
        }
        if (leaf_branch != null)
        {
            leaf_copy = leaf_branch.splitCopy();
        }
        event_chain noob = new event_chain(trunk_copy, leaf_copy);
        if (noob.trunk_branch == null)
        {
            if (noob.leaf_branch == null)
            {
                noob.thickness = thickness;
            }

        }
        foreach (Chronon content in linear_bit)
        {
            noob.Add(content);
        }
        return noob;
    }

    public double minimum_point_thickness()
    {
        if (trunk_branch == null)
        {
            if (leaf_branch == null)
            {
                return thickness;
            }
            else
            {
                return leaf_branch.minimum_point_thickness();
            }
        }
        else
        {
            if (leaf_branch == null)
            {
                return trunk_branch.minimum_point_thickness();
            }
            else
            {
                double a = trunk_branch.minimum_point_thickness();
                double b = leaf_branch.minimum_point_thickness();
                if (b > a)
                {
                    return a;
                }
                else
                {
                    return b;
                }
            }
        }
    }

    public List<Chronon> DisplayChronons(double clockhand)
    {
        double time_offset = clockhand;
        List<Chronon> basket = new List<Chronon>();
        if (trunk_branch != null)
        {
            if (time_offset < trunk_branch.thickness)
            {
                foreach (Chronon sap in trunk_branch.DisplayChronons(time_offset))
                {
                    basket.Add(sap);
                }
            }
            else
            {
                time_offset -= trunk_branch.thickness;
                if (leaf_branch != null)
                {
                    if (time_offset < leaf_branch.thickness)
                    {
                        foreach (Chronon sugar in leaf_branch.DisplayChronons(time_offset))
                        {
                            basket.Add(sugar);
                        }
                    }
                }
            }
        }
        else
        {
            if (leaf_branch != null)
            {
                if (time_offset < leaf_branch.thickness)
                {
                    foreach (Chronon sugar in leaf_branch.DisplayChronons(time_offset))
                    {
                        basket.Add(sugar);
                    }
                }
            }
        }
        foreach (Chronon peak in linear_bit)
        {
            basket.Add(peak);
        }
        return basket;

    }

    public double NextChange(double clockhand)
    {
        double time_offset = clockhand;
        if (trunk_branch != null)
        {
            if (time_offset < trunk_branch.thickness)
            {
                return trunk_branch.NextChange(time_offset);
            }
            else
            {
                time_offset -= trunk_branch.thickness;
            }
        }
        if (leaf_branch != null)
        {
            if (time_offset < leaf_branch.thickness)
            {
                return trunk_branch.thickness + leaf_branch.NextChange(time_offset);
            }
            else
            {
                Debug.Log("event_chain went to forbidden area "+ clockhand.ToString()+ " sst "+thickness.ToString()+" lolz "+time_offset);
                return time_offset - leaf_branch.thickness;
            }
        }
        return thickness;
    }


    public void renormalize(double factor)
    {
        double s = 0.0;
        if (trunk_branch!=null)
        {
            trunk_branch.renormalize(factor);
            s += trunk_branch.thickness;
        }
        if (leaf_branch != null)
        {
            leaf_branch.renormalize(factor);
            s += leaf_branch.thickness;
        }
        if (trunk_branch== null && leaf_branch == null)
        {
            thickness = thickness * factor;
            //Debug.Log("renorm" + thickness + ToString());
        }
        else
        {
            thickness = s;
        }
    }

    public void Add(Chronon present)
    {
        linear_bit.Add(present);
    }
}
