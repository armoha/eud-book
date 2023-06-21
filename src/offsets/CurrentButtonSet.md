
#  Current Button Set
Address   | 68C14C
----------|-------------
Player ID | 264058 (Byte Offset: 0)
Size 	  | 4
Length 	  | 1
SC:R      | Simple Data

The button set ID of the currently selected single unit. There is a 1-to-1 relationship between unit ID and it's button set, eg the buttonset for terran ghost is ID 1.

There are also several group buttonsets, for when multiple workers, or burrowable, or cloakable units etc selected:
* 244 - generic units, shows move/stop/attack/guard/patrol buttons
* 245 - workers, shows move/stock/attack + gather and return resources buttons
* 246 - cloakable units, as per 'generic' + cloak/decloak buttons
* 247 - burrowable units, as per 'generic' + burrow/unburrow buttons

Refer to button tabs in Firegraft.

Through experimentation, buttons occasionally have a delay of up to 2-3 seconds before changes in game state will update the button status (eg when a new tech is available, a button that relies on that tech may stay greyed out for 2-3 seconds). Setting this address with a different value (eg 244) is a way to force a refresh for the currently displayed button set.

Note that SC constantly updates this address to reflect the current unit's actual button set, to prevent units from being able to action commands that they shouldn't have access to (the infamous 1.13 patch series to stop any building from making any unit).
