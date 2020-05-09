SET @seq_counter := 0;	
SELECT * 
FROM

(SELECT
			( CASE     
				WHEN 

 DATE_FORMAT(t_seq.call_date_lead,"%i") 
					 - DATE_FORMAT(t_seq.call_date,"%i")
 <= 10 THEN 
				@seq_counter := @seq_counter + 1
				ELSE
				@seq_counter := @seq_counter 
				END
			)
		FROM
		(	SELECT iss.caller_id, iss.taken_by, iss.call_date, 
			LEAD(call_date,1) OVER (ORDER BY iss.call_date) AS call_date_lead
			FROM Issue iss 
			JOIN Caller cal
			ON (iss.caller_id = cal.caller_id)
			ORDER BY iss.call_date
		) AS t_seq 	
	) tt
;
