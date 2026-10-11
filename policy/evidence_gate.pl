% SWI-Prolog policy layer: model output is evidence, not authority.
% deterministic_gate_pass/fail come from validator/mrz_gate.py output.

decision(accept) :-
    gate(pass), uncertain_fields([]), human_readable_complete.
decision(need_better_evidence) :-
    gate(fail).
decision(escalate_to_human) :-
    gate(pass), ( uncertain_fields([_|_]) ; \+ human_readable_complete ).

% The model is never authorised to move a decision:
ai_authorised_to_override(false).
