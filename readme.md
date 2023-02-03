`get_all_todos():`
This is the home directry where all the different to do instructions are retrived using the get command


`create_todo`
This function creates a new post whenever one is entered usong the post request

`update_todo_by_id`
This function modifies a existing post based on the diven id using the patch request. The function accepts the ID of the todo that is to be updated and a todo request object that has the desired changes. The function then search for the matching todo object in your todo list and updates it with the received changes. The PATCH handler then responds with the entire todo object as it exists after being updated along with the `200 OK` status code. If there exists no todo object with the provided ID, the PATCH handler responds with a `404 Not Found` status code.

DELETE
`delete_todo_by_id`
This function deletes a post basd on the deleated id using the delete request. The function accepts the ID of the todo that should be deleted. The function then searches for the matching todo object in your todo list and remove it.



this code was written as an assignment to become more familiar with the FastAPI python framework where functions that will be used to handle incoming HTTP requests are created.

Mewtwo is an artificial Pokémon. It is a bipedal, humanoid Pokémon with some feline features. It is primarily gray with a long, purple tail. On top of its head are two short, blunt horns, and it has purple eyes. A tube extends from the back of its skull to the top of its spine, bypassing its neck. It has a defined chest and shoulders, which resemble a breastplate. The three digits on each hand and foot have spherical tips. Its tail is thick at the base but thins before ending in a small bulb. this pokeman shows bothe the cruel and creative side of humanity being that it is a artificial pokeman and that facinates me 