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
						title: 'All Day Event',
						start: new Date(y, m, 1)
					},
					{
						title: 'Long Event',
						start: new Date(y, m, d-5),
						end: new Date(y, m, d-2)
					},
					{
						id: 999,
						title: 'Repeating Event',
						start: new Date(y, m, d-3, 16, 0),
						allDay: false
					},
					{
						id: 999,
						title: 'Repeating Event',
						start: new Date(y, m, d+4, 16, 0),
						allDay: false
					},
					{
						title: 'Meeting',
						start: new Date(y, m, d, 10, 30),
						allDay: false
					},
					{
						title: 'Lunch',
						start: new Date(y, m, d, 12, 0),
						end: new Date(y, m, d, 14, 0),
						allDay: false
					},
					{
						title: 'Unavailable',
						start: new Date(y, m, d+1, 0, 0),
						end: new Date(y, m, d+1, 24, 0),
						allDay: false
					},
					{
						title: 'Click for Google',
						start: new Date(y, m, 28),
						end: new Date(y, m, 29),
						allDay: false
					},
					{
						title: 'Booked',
						start: new Date(y, m, d, 16, 0),
						end: new Date(y, m, d, 18, 0),
						allDay: false
					},
					{
						title: 'Booked',
						start: new Date(y, m, d, 14, 30),
						end: new Date(y, m, d, 15, 0),
						allDay: false
					},
					{
						title: 'Booked',
						start: new Date(y, m, d, 20, 0),
						end: new Date(y, m, d, 23, 0),
						allDay: false
					}
				]
			});
});
