document.addEventListener("readystatechange", (event) => {
	if (event.target.readyState === "interactive") {
		// Handles the filter form to redirect user to proper filter url
		document.getElementById('filterForm').addEventListener('submit', function(event) {
			event.preventDefault();
			var minElo = document.getElementById('elo_low').value;
			if (minElo === "") minElo = "0";
			var maxElo = document.getElementById('elo_high').value;
			if (maxElo === "") maxElo = "100000";
			var completed = document.getElementById('completed').checked;
			if (completed) completed = "1";
			else completed = "0";
			var tags = document.getElementById('tags').value;
			if (tags === ""){
				var location = `/problems/${minElo}/${maxElo}/${completed}/`;
			}
			else {
				var location = `/problems/${minElo}/${maxElo}/${completed}/${tags}/`;
			}
			window.location.href = location;
		});
	}
});
