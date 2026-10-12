# Character definition
define y = Character("You")
define d = Character("Person D")

# HUD display
default empathy_score = 0
default support_score = 0
default accountability_score = 0

screen confidence_ui():
    vbox:
        xalign 0.98
        yalign 0.02
        spacing 5

        frame:
            text "Empathy Score (Understand the individual's circumstances without making assumptions): [empathy_score]"

        frame:
            text "Support Score (Offers appropriate help and collaborates on realistic adjustments): [support_score]"

        frame:
            text "Accountability (Addresses the effect on colleagues and agrees clear expectations): [accountability_score]"

scene black
with fade

"Thursday, 5:30 PM."

"You arrive at a charity meeting expecting to review the plans for an upcoming event. Instead, you find yourself looking at an incomplete spreadsheet, three unanswered messages, and a list of tasks that should have been finished earlier in the week."

y "{i}Right. The event is next Saturday. The promotional materials aren't finished, the volunteer rota is incomplete, and the person who was coordinating the bookings hasn't responded to the group chat since Monday.{/i}"

y "{i}That person is Person D. They've always been reliable before, which makes the sudden change difficult to understand.{/i}"

"You sit down and open the task tracker. Several of Person D's assigned tasks are marked as incomplete."

y "{i}I don't know what's happened. Maybe they're overwhelmed. Maybe they've lost interest. Maybe they've simply forgotten. I should probably avoid writing an entire fictional biography about someone based on three unanswered messages.{/i}"

"A few minutes later, Person D arrives."

d "Hey. Sorry I'm late."

y "No problem. We were just looking at the event preparations."

d "Right. About those..."

"Person D sits down and looks at the task tracker."

d "I know I've fallen behind. I was supposed to finish the promotional materials and confirm the volunteer rota, but I haven't managed to get them done."

y "Is everything okay?"

d "Yeah. Well, not really. I've just had a lot going on lately."

"Person D looks away, then begins fiddling with their phone."

d "I know that's not an excuse. Everyone else has been working hard, and I've left people with extra work. I'm sorry."

y "{i}They're acknowledging the problem, but they haven't explained what's going on. I could press them for details, tell them they need to get their act together, or give them space to explain what they're comfortable sharing.{/i}"

y "{i}As a Trustee, I need to care about the people doing the work. But I also need to consider the team members who are covering the unfinished tasks. Their time matters too.{/i}"

menu:
    "How do you respond to Person D?"

    "Tell Person D that the team needs them to start delivering on their commitments.":
        $ empathy_score -= 1
        $ support_score -= 1
        $ accountability_score += 1

        y "I appreciate you being honest, but we need these tasks completed. Other people are having to pick up the work, and that's putting pressure on the team."

        d "I know. I've been feeling terrible about it."

        y "Then we need to make sure it doesn't keep happening."

        d "Okay. I'll try to get things sorted."

        y "{i}I've addressed the impact on the team, which is important. But I haven't really explored why Person D is struggling or whether there's a practical way to help them recover.{/i}"

        y "{i}Accountability matters, but if the conversation ends with someone feeling worse and no clearer plan, we haven't solved much.{/i}"

    "Ask how they're doing and give them room to explain.":
        $ empathy_score += 2
        $ support_score += 1
        $ accountability_score += 0

        y "You don't have to explain anything you're uncomfortable sharing, but I'm concerned about you. How have things been lately?"

        d "Honestly? Pretty difficult."

        y "I'm sorry to hear that. Do you want to talk about what's been making things difficult?"

        d "A bit, yeah. I just didn't know how to bring it up."

        y "{i}I'm not assuming I know the answer. I'm giving Person D an opportunity to explain their situation without having to defend themselves immediately.{/i}"

        y "{i}I still need to understand what happens with the unfinished work, but I don't need to solve that before I've listened.{/i}"

    "Avoid discussing it and move straight to the event agenda.":
        $ empathy_score -= 1
        $ support_score -= 1
        $ accountability_score -= 1

        y "We can discuss that another time. Let's get through the agenda first."

        d "Sure."

        "Person D opens the agenda but barely looks at it."

        y "{i}I've avoided an uncomfortable conversation, but the problem hasn't disappeared. Person D is still struggling, and the team still has unfinished work.{/i}"

        y "{i}Keeping a meeting moving can be useful. Ignoring an issue that directly affects the team is a different matter.{/i}"

"Person D takes a breath."

d "I've been dealing with some difficult stuff at home. Someone in my family needs more support at the moment, and I've been helping them whenever I can."

d "It's been affecting my sleep, and I've struggled to concentrate. I keep telling myself I'll catch up tomorrow, but then something else happens."

d "I didn't want to tell everyone because it's personal. And I didn't want people thinking I couldn't handle being involved in the charity."

y "{i}That changes the picture. Person D isn't necessarily being careless or disengaged. They may be trying to manage more than they can reasonably handle.{/i}"

y "{i}At the same time, the team cannot plan around information it doesn't have. If commitments repeatedly go unfinished, someone else has to absorb the consequences.{/i}"

y "Thanks for telling me. You don't need to share more personal details than you're comfortable with."

d "I appreciate that. I just don't know what to do about the event. I still want to help, but I can't promise I'll suddenly have loads of free time."

y "That's fair. Let's look at what's still outstanding and work out what is realistic."

d "I can probably finish the promotional materials, but the volunteer rota might be too much. I haven't even checked everyone's availability properly."

y "{i}This is where good intentions need to turn into an actual plan. Reassuring Person D is one thing. Making sure the event can still run is another.{/i}"

y "{i}I need to avoid two extremes: expecting them to carry on as normal, or removing all their responsibilities without discussing what they can still manage.{/i}"

menu:
    "How do you help Person D manage their workload?"

    "Take all their tasks away immediately so they can focus on their personal situation.":
        $ empathy_score += 1
        $ support_score += 1
        $ accountability_score -= 1

        y "Don't worry about the event. We'll take everything off your hands and sort it ourselves."

        d "Are you sure? I don't want to leave everyone else with even more work."

        y "We'll manage somehow."

        d "I appreciate it, but I'd still like to contribute if I can."

        y "{i}I'm trying to be supportive, but I've made the decision for Person D without asking what they feel able to do. I've also promised that the team can absorb the extra work without checking whether that's realistic.{/i}"

        y "{i}Support should give people options, not automatically remove their agency. I also need to make sure the remaining workload is fairly distributed.{/i}"

    "Agree on a smaller workload and redistribute the remaining tasks openly.":
        $ empathy_score += 1
        $ support_score += 2
        $ accountability_score += 2

        y "What if we keep the promotional materials with you, since you think that's manageable, and move the volunteer rota to someone with more availability?"

        y "We can also tell the team what's changing without sharing your private circumstances."

        d "That would help. I can focus on one thing instead of worrying about both."

        y "Let's agree on a realistic deadline for the materials, and we'll check in before then. If your situation changes, tell me as early as you can so we can adjust."

        d "I can do that. Thank you for not making me feel like I've failed at everything."

        y "You're dealing with a difficult situation. We still need to organise the work, but we can do that without making it personal."

        y "{i}This feels more balanced. Person D retains a meaningful contribution, the team knows what needs covering, and we've agreed on a way to communicate if things change.{/i}"

    "Tell Person D to take a break and return when they can manage everything again.":
        $ empathy_score += 0
        $ support_score -= 1
        $ accountability_score -= 1

        y "Maybe you should step away until things settle down. Come back when you're able to manage the full workload."

        d "I don't know how long that will be. I don't really want to leave completely."

        y "I just think it's better than trying to do everything badly."

        d "I suppose."

        y "{i}A break might be appropriate, but I've presented it as an all-or-nothing decision. I haven't explored whether a smaller role or temporary adjustment would work better.{/i}"

        y "{i}People shouldn't have to choose between doing everything and contributing nothing. Sometimes a little flexibility makes continued involvement possible.{/i}"

"Friday, 11:15 AM."

"You send a short message to the Trustees explaining that the volunteer rota needs to be reassigned and that the promotional materials have a revised deadline. You don't disclose Person D's private circumstances."

"The response is mixed. One Trustee offers to help with the rota. Another expresses frustration."

"Later that afternoon, Person D messages you."

d "Just wanted to say thanks for yesterday. I've started working on the promotional materials. I think having one clear task will help."

y "{i}Good. We have a plan, and Person D seems more comfortable. But one conversation doesn't magically fix everything. I need to see whether the arrangement is working and whether the rest of the team is coping.{/i}"

"You arrange a short check-in before the event."

"Saturday, 10:00 AM. One week before the event."

"You meet Person D to review progress."

d "The promotional materials are nearly done. I should be able to finish them tonight."

y "That's good progress. How is the rest of your workload looking?"

d "Still difficult, to be honest. I don't want to promise that everything is sorted, because it isn't."

y "{i}This is a moment where I could mistake honesty for a lack of commitment. But Person D is communicating earlier than before, which gives us more time to respond.{/i}"

d "I also heard that someone else had to spend their evening sorting out the rota. I feel bad about that."

y "It's understandable to feel bad, but we should focus on what we can do now. We need to make sure the person who helped isn't left carrying an unfair amount of extra work."

d "I agree. Is there anything I can do to help them, even if I can't take the rota back?"

y "{i}That's encouraging. Person D is thinking about the wider team, not just their own situation. Now I need to help turn that into something practical.{/i}"

menu:
    "How do you respond to Person D's offer?"

    "Tell them not to worry about the team and focus only on themselves.":
        $ empathy_score += 1
        $ support_score += 1
        $ accountability_score -= 1

        y "Don't worry about anyone else. Just focus on yourself until things get better."

        d "I appreciate that, but I would still like to do something to help."

        y "I don't want you putting more pressure on yourself."

        d "I understand. I just don't want the others to think I don't care."

        y "{i}I'm trying to protect Person D from further pressure, but I'm not taking their wish to contribute seriously. Supporting someone includes listening to what they want to offer, not only deciding what they should avoid.{/i}"

    "Ask what they could realistically contribute and check with the affected Trustee.":
        $ empathy_score += 1
        $ support_score += 1
        $ accountability_score += 2

        y "Let's work out what you could realistically manage without putting your other commitments at risk."

        y "You could offer to help with one small task, but let's check with the person who handled the rota first. We shouldn't assume they need help in a particular way."

        d "That sounds fair. I could help prepare the volunteer information packs once the rota is finalised."

        y "Good. I'll ask whether that would be useful, and we can agree on a deadline that works for you."

        d "Thanks. I feel better knowing there's a way I can contribute without taking on too much."

        y "{i}We're considering Person D's capacity, the other Trustee's workload, and what the event needs. Nobody has to guess what the others can manage.{/i}"

    "Tell Person D that they owe the team extra work to make up for falling behind.":
        $ empathy_score -= 1
        $ support_score -= 1
        $ accountability_score += 0

        y "The team has had to cover for you, so it would be fair for you to take on some extra work."

        d "I understand why you're saying that, but I'm not sure I can promise anything extra right now."

        y "Then we'll have to see what can be done."

        d "Okay."

        y "{i}It's reasonable to care about fairness, but treating extra work as repayment risks ignoring the circumstances that caused the problem in the first place.{/i}"

        y "{i}Fairness doesn't always mean everyone does the same amount of work. It means being transparent about responsibilities and making sure the arrangement is sustainable for everyone.{/i}"

"The following week, the event preparations continue. The promotional materials are completed, the rota is covered, and the Trustees have a clearer understanding of the remaining work."

d "I know things weren't ideal recently. I'm going to try to give more notice if I'm struggling in future."

y "That would help. And if you need to change what you can take on, tell us early so we can plan around it."

d "I can do that. I don't want people having to guess what's happening."

y "{i}I can't know exactly how things will go from here. Person D may need more support in the future, and the team may face another difficult deadline.{/i}"

y "{i}But we have a better approach now: listen before assuming, agree on realistic commitments, and communicate changes before they become emergencies.{/i}"

y "{i}Human-centred leadership doesn't mean removing every difficulty from someone's life. It means treating people with dignity while making thoughtful decisions about the responsibilities we share.{/i}"

"You close the task tracker."

y "{i}And perhaps next time, we can organise an event without discovering three new problems in the final week. I remain cautiously optimistic.{/i}"
