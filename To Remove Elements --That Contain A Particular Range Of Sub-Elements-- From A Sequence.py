## IDLE (Python 3.8.0)

## To Remove Elements --That Contain A Particular Range Of Sub-Elements-- From A Sequence

LR =    ## [list] <<----
## LR means List Removed (List that contain elements that will be Removed)
LC =    ## [list] <<----
## LC means List Criteria (List that contain elements that equal the criteria used to determine the elements that will be removed)
InSFr =    ## [index] <<----
## InSFr means Index Slice First. If there's no number then use keyword: None.
InSSc =    ## [index] <<----
## InSSc means Index Slice Second. If there's no number then use keyword: None.

for ItLR in LR:
    for ItLC in LC:
        if ItLC == ItLR[InSFr:InSSc]:
            LR.remove(ItLR)
