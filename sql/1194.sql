select group_id, player_id from
    (select p.group_id, m.player_id, sum(m.score) as score
    from 
        (select first_player as player_id, first_score as score
        from matches
        union all
        select second_player as player_id, second_score as score
        from matches) m
        join players p
    on m.player_id = p.player_id
    group by m.player_id order by group_id, score desc, player_id) top_scores
group by group_id