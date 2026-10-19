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
            text "Accountability Score (Addresses the effect on colleagues and agrees clear expectations): [accountability_score]"
label start:

    show screen confidence_ui

    play sound "voice_lines/1.mp3"
    "Welcome! To continue, please press left click on your mouse / tap your mousepad or screen while your cursor is on the game."

    play sound "voice_lines/2.mp3"
    "Great! This is a simulated scenario based on Providing Support."

    play sound "voice_lines/3.mp3"
    "Please note that this is a fictional video game, and there are no real names used."

    play sound "voice_lines/4.mp3"
    "During the game, you will have the option to 'choose your response' through key points."

    play sound "voice_lines/5.mp3"
    "There are no right or wrong answers, and many options will increase one or more scores while lowering others. That is life!"

    play sound "voice_lines/6.mp3"
    "Once you are ready, press left click one more time and the simulated scenario will start!"

    # Scenario Start

    play sound "voice_lines/7.mp3"
    "Providing Support: Scenario Start!"

scene black
with fade

play sound "voice_lines/8.mp3"
"Thursday, 5:30 PM."

play sound "voice_lines/9.mp3"
"You arrive at a charity meeting expecting to review the plans for an upcoming event. Instead, you find yourself looking at an incomplete spreadsheet, three unanswered messages, and a list of tasks that should have been finished earlier in the week."

play sound "voice_lines/10.mp3"
y "{i}Right. The event is next Saturday. The promotional materials aren't finished, the volunteer rota is incomplete, and the person who was coordinating the bookings hasn't responded to the group chat since Monday.{/i}"

play sound "voice_lines/11.mp3"
y "{i}That person is Person D. They've always been reliable before, which makes the sudden change difficult to understand.{/i}"

play sound "voice_lines/12.mp3"
"You sit down and open the task tracker. Several of Person D's assigned tasks are marked as incomplete."

play sound "voice_lines/13.mp3"
y "{i}I don't know what's happened. Maybe they're overwhelmed. Maybe they've lost interest. Maybe they've simply forgotten. I should probably avoid writing an entire fictional biography about someone based on three unanswered messages.{/i}"

play sound "voice_lines/14.mp3"
"A few minutes later, Person D arrives."

play sound "voice_lines/15.mp3"
d "Hey. Sorry I'm late."

play sound "voice_lines/16.mp3"
y "No problem. We were just looking at the event preparations."

play sound "voice_lines/17.mp3"
d "Right. About those..."

play sound "voice_lines/18.mp3"
"Person D sits down and looks at the task tracker."

play sound "voice_lines/19.mp3"
d "I know I've fallen behind. I was supposed to finish the promotional materials and confirm the volunteer rota, but I haven't managed to get them done."

play sound "voice_lines/20.mp3"
y "Is everything okay?"

play sound "voice_lines/21.mp3"
d "Yeah. Well, not really. I've just had a lot going on lately."

play sound "voice_lines/22.mp3"
"Person D looks away, then begins fiddling with their phone."

play sound "voice_lines/23.mp3"
d "I know that's not an excuse. Everyone else has been working hard, and I've left people with extra work. I'm sorry."

play sound "voice_lines/24.mp3"
y "{i}They're acknowledging the problem, but they haven't explained what's going on. I could press them for details, tell them they need to get their act together, or give them space to explain what they're comfortable sharing.{/i}"

play sound "voice_lines/25.mp3"
y "{i}As a Trustee, I need to care about the people doing the work. But I also need to consider the team members who are covering the unfinished tasks. Their time matters too.{/i}"

menu:
    "How do you respond to Person D?"

    "Tell Person D that the team needs them to start delivering on their commitments.":
        $ empathy_score -= 1
        $ support_score -= 1
        $ accountability_score += 1

        play sound "voice_lines/26.mp3"
        y "I appreciate you being honest, but we need these tasks completed. Other people are having to pick up the work, and that's putting pressure on the team."

        play sound "voice_lines/27.mp3"
        d "I know. I've been feeling terrible about it."

        play sound "voice_lines/28.mp3"
        y "Then we need to make sure it doesn't keep happening."

        play sound "voice_lines/29.mp3"
        d "Okay. I'll try to get things sorted."

        play sound "voice_lines/30.mp3"
        y "{i}I've addressed the impact on the team, which is important. But I haven't really explored why Person D is struggling or whether there's a practical way to help them recover.{/i}"

        play sound "voice_lines/31.mp3"
        y "{i}Accountability matters, but if the conversation ends with someone feeling worse and no clearer plan, we haven't solved much.{/i}"

    "Ask how they're doing and give them room to explain.":
        $ empathy_score += 2
        $ support_score += 1
        $ accountability_score += 0

        play sound "voice_lines/32.mp3"
        y "You don't have to explain anything you're uncomfortable sharing, but I'm concerned about you. How have things been lately?"

        play sound "voice_lines/33.mp3"
        d "Honestly? Pretty difficult."

        play sound "voice_lines/34.mp3"
        y "I'm sorry to hear that. Do you want to talk about what's been making things difficult?"

        play sound "voice_lines/35.mp3"
        d "A bit, yeah. I just didn't know how to bring it up."

        play sound "voice_lines/36.mp3"
        y "{i}I'm not assuming I know the answer. I'm giving Person D an opportunity to explain their situation without having to defend themselves immediately.{/i}"

        play sound "voice_lines/37.mp3"
        y "{i}I still need to understand what happens with the unfinished work, but I don't need to solve that before I've listened.{/i}"

    "Avoid discussing it and move straight to the event agenda.":
        $ empathy_score -= 1
        $ support_score -= 1
        $ accountability_score -= 1

        play sound "voice_lines/38.mp3"
        y "We can discuss that another time. Let's get through the agenda first."

        play sound "voice_lines/39.mp3"
        d "Sure."

        play sound "voice_lines/40.mp3"
        "Person D opens the agenda but barely looks at it."

        play sound "voice_lines/41.mp3"
        y "{i}I've avoided an uncomfortable conversation, but the problem hasn't disappeared. Person D is still struggling, and the team still has unfinished work.{/i}"

        play sound "voice_lines/42.mp3"
        y "{i}Keeping a meeting moving can be useful. Ignoring an issue that directly affects the team is a different matter.{/i}"

play sound "voice_lines/43.mp3"
"Person D takes a breath."

play sound "voice_lines/44.mp3"
d "I've been dealing with some difficult stuff at home. Someone in my family needs more support at the moment, and I've been helping them whenever I can."

play sound "voice_lines/45.mp3"
d "It's been affecting my sleep, and I've struggled to concentrate. I keep telling myself I'll catch up tomorrow, but then something else happens."

play sound "voice_lines/46.mp3"
d "I didn't want to tell everyone because it's personal. And I didn't want people thinking I couldn't handle being involved in the charity."

play sound "voice_lines/47.mp3"
y "{i}That changes the picture. Person D isn't necessarily being careless or disengaged. They may be trying to manage more than they can reasonably handle.{/i}"

play sound "voice_lines/48.mp3"
y "{i}At the same time, the team cannot plan around information it doesn't have. If commitments repeatedly go unfinished, someone else has to absorb the consequences.{/i}"

play sound "voice_lines/49.mp3"
y "Thanks for telling me. You don't need to share more personal details than you're comfortable with."

play sound "voice_lines/50.mp3"
d "I appreciate that. I just don't know what to do about the event. I still want to help, but I can't promise I'll suddenly have loads of free time."

play sound "voice_lines/51.mp3"
y "That's fair. Let's look at what's still outstanding and work out what is realistic."

play sound "voice_lines/52.mp3"
d "I can probably finish the promotional materials, but the volunteer rota might be too much. I haven't even checked everyone's availability properly."

play sound "voice_lines/53.mp3"
y "{i}This is where good intentions need to turn into an actual plan. Reassuring Person D is one thing. Making sure the event can still run is another.{/i}"

play sound "voice_lines/54.mp3"
y "{i}I need to avoid two extremes: expecting them to carry on as normal, or removing all their responsibilities without discussing what they can still manage.{/i}"

menu:
    "How do you help Person D manage their workload?"

    "Take all their tasks away immediately so they can focus on their personal situation.":
        $ empathy_score += 1
        $ support_score += 1
        $ accountability_score -= 1

        play sound "voice_lines/55.mp3"
        y "Don't worry about the event. We'll take everything off your hands and sort it ourselves."

        play sound "voice_lines/56.mp3"
        d "Are you sure? I don't want to leave everyone else with even more work."

        play sound "voice_lines/57.mp3"
        y "We'll manage somehow."

        play sound "voice_lines/58.mp3"
        d "I appreciate it, but I'd still like to contribute if I can."

        play sound "voice_lines/59.mp3"
        y "{i}I'm trying to be supportive, but I've made the decision for Person D without asking what they feel able to do. I've also promised that the team can absorb the extra work without checking whether that's realistic.{/i}"

        play sound "voice_lines/60.mp3"
        y "{i}Support should give people options, not automatically remove their agency. I also need to make sure the remaining workload is fairly distributed.{/i}"

    "Agree on a smaller workload and redistribute the remaining tasks openly.":
        $ empathy_score += 1
        $ support_score += 2
        $ accountability_score += 2

        play sound "voice_lines/61.mp3"
        y "What if we keep the promotional materials with you, since you think that's manageable, and move the volunteer rota to someone with more availability?"

        play sound "voice_lines/62.mp3"
        y "We can also tell the team what's changing without sharing your private circumstances."

        play sound "voice_lines/63.mp3"
        d "That would help. I can focus on one thing instead of worrying about both."

        play sound "voice_lines/64.mp3"
        y "Let's agree on a realistic deadline for the materials, and we'll check in before then. If your situation changes, tell me as early as you can so we can adjust."

        play sound "voice_lines/65.mp3"
        d "I can do that. Thank you for not making me feel like I've failed at everything."

        play sound "voice_lines/66.mp3"
        y "You're dealing with a difficult situation. We still need to organise the work, but we can do that without making it personal."

        play sound "voice_lines/67.mp3"
        y "{i}This feels more balanced. Person D retains a meaningful contribution, the team knows what needs covering, and we've agreed on a way to communicate if things change.{/i}"

    "Tell Person D to take a break and return when they can manage everything again.":
        $ empathy_score += 0
        $ support_score -= 1
        $ accountability_score -= 1

        play sound "voice_lines/68.mp3"
        y "Maybe you should step away until things settle down. Come back when you're able to manage the full workload."

        play sound "voice_lines/69.mp3"
        d "I don't know how long that will be. I don't really want to leave completely."

        play sound "voice_lines/70.mp3"
        y "I just think it's better than trying to do everything badly."

        play sound "voice_lines/71.mp3"
        d "I suppose."

        play sound "voice_lines/72.mp3"
        y "{i}A break might be appropriate, but I've presented it as an all-or-nothing decision. I haven't explored whether a smaller role or temporary adjustment would work better.{/i}"

        play sound "voice_lines/73.mp3"
        y "{i}People shouldn't have to choose between doing everything and contributing nothing. Sometimes a little flexibility makes continued involvement possible.{/i}"

play sound "voice_lines/74.mp3"
"Friday, 11:15 AM."

play sound "voice_lines/75.mp3"
"You send a short message to the Trustees explaining that the volunteer rota needs to be reassigned and that the promotional materials have a revised deadline. You don't disclose Person D's private circumstances."

play sound "voice_lines/76.mp3"
"The response is mixed. One Trustee offers to help with the rota. Another expresses frustration."

play sound "voice_lines/77.mp3"
"Later that afternoon, Person D messages you."

play sound "voice_lines/78.mp3"
d "Just wanted to say thanks for yesterday. I've started working on the promotional materials. I think having one clear task will help."

play sound "voice_lines/79.mp3"
y "{i}Good. We have a plan, and Person D seems more comfortable. But one conversation doesn't magically fix everything. I need to see whether the arrangement is working and whether the rest of the team is coping.{/i}"

play sound "voice_lines/80.mp3"
"You arrange a short check-in before the event."

play sound "voice_lines/81.mp3"
"Saturday, 10:00 AM. One week before the event."

play sound "voice_lines/82.mp3"
"You meet Person D to review progress."

play sound "voice_lines/83.mp3"
d "The promotional materials are nearly done. I should be able to finish them tonight."

play sound "voice_lines/84.mp3"
y "That's good progress. How is the rest of your workload looking?"

play sound "voice_lines/85.mp3"
d "Still difficult, to be honest. I don't want to promise that everything is sorted, because it isn't."

play sound "voice_lines/86.mp3"
y "{i}This is a moment where I could mistake honesty for a lack of commitment. But Person D is communicating earlier than before, which gives us more time to respond.{/i}"

play sound "voice_lines/87.mp3"
d "I also heard that someone else had to spend their evening sorting out the rota. I feel bad about that."

play sound "voice_lines/88.mp3"
y "It's understandable to feel bad, but we should focus on what we can do now. We need to make sure the person who helped isn't left carrying an unfair amount of extra work."

play sound "voice_lines/89.mp3"
d "I agree. Is there anything I can do to help them, even if I can't take the rota back?"

play sound "voice_lines/90.mp3"
y "{i}That's encouraging. Person D is thinking about the wider team, not just their own situation. Now I need to help turn that into something practical.{/i}"

menu:
    "How do you respond to Person D's offer?"

    "Tell them not to worry about the team and focus only on themselves.":
        $ empathy_score += 1
        $ support_score += 1
        $ accountability_score -= 1

        play sound "voice_lines/91.mp3"
        y "Don't worry about anyone else. Just focus on yourself until things get better."

        play sound "voice_lines/92.mp3"
        d "I appreciate that, but I would still like to do something to help."

        play sound "voice_lines/93.mp3"
        y "I don't want you putting more pressure on yourself."

        play sound "voice_lines/94.mp3"
        d "I understand. I just don't want the others to think I don't care."

        play sound "voice_lines/95.mp3"
        y "{i}I'm trying to protect Person D from further pressure, but I'm not taking their wish to contribute seriously. Supporting someone includes listening to what they want to offer, not only deciding what they should avoid.{/i}"

    "Ask what they could realistically contribute and check with the affected Trustee.":
        $ empathy_score += 1
        $ support_score += 1
        $ accountability_score += 1

        play sound "voice_lines/96.mp3"
        y "Let's work out what you could realistically manage without putting your other commitments at risk."

        play sound "voice_lines/97.mp3"
        y "You could offer to help with one small task, but let's check with the person who handled the rota first. We shouldn't assume they need help in a particular way."

        play sound "voice_lines/98.mp3"
        d "That sounds fair. I could help prepare the volunteer information packs once the rota is finalised."

        play sound "voice_lines/99.mp3"
        y "Good. I'll ask whether that would be useful, and we can agree on a deadline that works for you."

        play sound "voice_lines/100.mp3"
        d "Thanks. I feel better knowing there's a way I can contribute without taking on too much."

        play sound "voice_lines/101.mp3"
        y "{i}We're considering Person D's capacity, the other Trustee's workload, and what the event needs. Nobody has to guess what the others can manage.{/i}"

    "Tell Person D that they owe the team extra work to make up for falling behind.":
        $ empathy_score -= 1
        $ support_score -= 1
        $ accountability_score += 0

        play sound "voice_lines/102.mp3"
        y "The team has had to cover for you, so it would be fair for you to take on some extra work."

        play sound "voice_lines/103.mp3"
        d "I understand why you're saying that, but I'm not sure I can promise anything extra right now."

        play sound "voice_lines/104.mp3"
        y "Then we'll have to see what can be done."

        play sound "voice_lines/105.mp3"
        d "Okay."

        play sound "voice_lines/106.mp3"
        y "{i}It's reasonable to care about fairness, but treating extra work as repayment risks ignoring the circumstances that caused the problem in the first place.{/i}"

        #play sound "voice_lines/107.mp3"
        y "{i}Fairness doesn't always mean everyone does the same amount of work. It means being transparent about responsibilities and making sure the arrangement is sustainable for everyone.{/i}"

#play sound "voice_lines/108.mp3"
"The following week, the event preparations continue. The promotional materials are completed, the rota is covered, and the Trustees have a clearer understanding of the remaining work."

#play sound "voice_lines/109.mp3"
d "I know things weren't ideal recently. I'm going to try to give more notice if I'm struggling in future."

#play sound "voice_lines/110.mp3"
y "That would help. And if you need to change what you can take on, tell us early so we can plan around it."

#play sound "voice_lines/111.mp3"
d "I can do that. I don't want people having to guess what's happening."

# Personal endings
#play sound "voice_lines/112.mp3"
"Your choices impacted your empathy to others, the level of support and the amount of accountability you provided"

# Empathy
if empathy_score < 0:

    #play sound "voice_lines/113.mp3"
    "Your choices suggest that you may not have fully considered how Person D was experiencing their situation."
    
    #play sound "voice_lines/114.mp3"
    "When someone is facing a challenge, it can be easy to make assumptions."

    #play sound "voice_lines/115.mp3"
    "Advice: Take time to listen before offering solutions."

    #play sound "voice_lines/116.mp3"
    "Ask open questions, avoid making assumptions about someone's circumstances, and acknowledge their perspective."

elif empathy_score == 0:

    #play sound "voice_lines/117.mp3"
    "Your choices suggest a mixed approach to understanding Person D's situation." 
    
    #play sound "voice_lines/118.mp3"
    "You may have recognised some of their difficulties while overlooking other factors"

    #play sound "voice_lines/119.mp3"
    "Advice: Try to understand both the practical and emotional aspects of someone's situation."

else:

    #play sound "voice_lines/120.mp3"
    "Your choices suggest that you made an effort to understand Person D's perspective and recognise the challenges they were experiencing."

    #play sound "voice_lines/121.mp3"
    "Advice: Continue listening without judgement and acknowledging people's experiences."

    #play sound "voice_lines/122.mp3"
    "Remember that empathy does not require you to agree with every decision someone makes."

# Support
if support_score < 0:

    #play sound "voice_lines/123.mp3"
    "Your choices suggest that the support offered to Person D may not have fully addressed their needs."

    #play sound "voice_lines/124.mp3"
    "Dismissing difficulties or leaving someone to manage everything alone can make an already challenging situation harder."

    play sound "voice_lines/125.mp3"
    "Advice: Ask what support would be useful before deciding what to do."

    play sound "voice_lines/126.mp3"
    "Explore practical options and agree on realistic next steps."

elif support_score == 0:

    play sound "voice_lines/127.mp3"
    "Your choices suggest that you recognised the need to support Person D, but there may have been uncertainty about the most appropriate way to help."

    play sound "voice_lines/128.mp3"
    "Advice: Discuss possible options together and agree on what is achievable."

    play sound "voice_lines/129.mp3"
    "Avoid taking over responsibilities unnecessarily, but do not assume that someone can manage without help."

else:
    
    play sound "voice_lines/130.mp3"
    "Your choices suggest that you considered how to help Person D in a constructive and considerate way."

    play sound "voice_lines/131.mp3"
    "Advice: Continue offering practical help while involving the person in decisions about their own situation."

    #play sound "voice_lines/132.mp3"
    "Agree on clear next steps, respect their preferences and check whether the support is working."

# Accountability
if accountability_score < 0:

    #play sound "voice_lines/133.mp3"
    "Your choices suggest that responsibilities or expectations may not have been addressed clearly enough."

    #play sound "voice_lines/134.mp3"
    "Avoiding a difficult conversation or failing to follow up can create uncertainty and affect other people in the charity."

    #play sound "voice_lines/135.mp3"
    "Advice: Be honest about what can realistically be achieved."

    #play sound "voice_lines/136.mp3"
    "Accountability should address the situation fairly without blaming someone for experiencing difficulties."

elif accountability_score == 0:

    #play sound "voice_lines/137.mp3"
    "Your choices suggest that you attempted to balance understanding Person D's circumstances with maintaining their responsibilities."

    #play sound "voice_lines/138.mp3"
    "Advice: Combine understanding with clear communication. Agree on achievable commitments and identify any adjustments that may be needed."

    #play sound "voice_lines/139.mp3"
    "Supporting someone and maintaining accountability can work together."

else:
    
    #play sound "voice_lines/140.mp3"
    "Your choices suggest that you considered both Person D's circumstances and the responsibilities involved."

    #play sound "voice_lines/141.mp3"
    "Advice: Continue setting clear, realistic expectations and following through on agreed actions."

    #play sound "voice_lines/142.mp3"
    "As a trustee, remember that accountability is about responsible decision-making and learning, not simply assigning blame."

#play sound "voice_lines/143.mp3"
y "{i}I can't know exactly how things will go from here. Person D may need more support in the future, and the team may face another difficult deadline.{/i}"

#play sound "voice_lines/144.mp3"
y "{i}But we have a better approach now: listen before assuming, agree on realistic commitments, and communicate changes before they become emergencies.{/i}"

#play sound "voice_lines/145.mp3"
y "{i}Human-centred leadership doesn't mean removing every difficulty from someone's life. It means treating people with dignity while making thoughtful decisions about the responsibilities we share.{/i}"

#play sound "voice_lines/146.mp3"
"You close the task tracker."

#play sound "voice_lines/147.mp3"
y "{i}And perhaps next time, we can organise an event without discovering three new problems in the final week. I remain cautiously optimistic.{/i}"
