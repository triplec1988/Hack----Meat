$(window).load(function(){
    // $('.splash-title').fitText();
    var date = new Date();
			var d = date.getDate();
			var m = date.getMonth();
			var y = date.getFullYear();
			
			var calendar = $('#calendar').fullCalendar({
				header: {
					left: 'prev,next today',
					center: 'title',
					right: 'month,agendaWeek,agendaDay'
				},
				defaultView: 'agendaWeek',
				selectable: true,
				selectHelper: true,
				select: function(start, end, allDay) {
					var title = prompt('Event Title:');
					if (title) {
						calendar.fullCalendar('renderEvent',
							{
								title: title,
								start: start,
								end: end,
								allDay: allDay
							},
							true // make the event "stick"
						);
					}
					calendar.fullCalendar('unselect');
				},
				editable: true,
				events: [
					{
						title: 'Unavailable',
						start: new Date(y, m, d-5),
						end: new Date(y, m, d-2)
					},
					{
						id: 999,
						title: 'Unavailable',
						start: new Date(y, m, d-3, 16, 0),
						allDay: false
					},
					{
						title: 'Unavailable',
						start: new Date(y, m, d, 12, 0),
						end: new Date(y, m, d, 14, 0),
						allDay: false
					},
					{
						title: 'Unavailable',
						start: new Date(y, m, d, 14, 30),
						end: new Date(y, m, d, 19, 0),
						allDay: false
					},
					{
						title: 'Unavailable',
						start: new Date(y, m, d+1, 12, 30),
						end: new Date(y, m, d+1, 17, 0),
						allDay: false
					},
					{
						title: 'Unavailable',
						start: new Date(y, m, d+1, 8, 30),
						end: new Date(y, m, d+1, 11, 0),
						allDay: false
					},
					{
						title: 'Unavailable',
						start: new Date(y, m, d+2, 7, 30),
						end: new Date(y, m, d+2, 13, 0),
						allDay: false
					},
					
					{
						title: 'Unavailable',
						start: new Date(y, m, d+3, 9, 0),
						end: new Date(y, m, d+3, 17, 0),
						allDay: false
					},
					{
						title: 'Unavailable',
						start: new Date(y, m, d+4, 15, 0),
						end: new Date(y, m, d+4, 17, 0),
						allDay: false
					},
					{
						title: 'Unavailable',
						start: new Date(y, m, d+5, 9, 0),
						end: new Date(y, m, d+5, 14, 0),
						allDay: false
					},


					
				]
			});
});
