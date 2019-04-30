from django.test import TestCase

# Create your tests here.





  <section class="float-left">
    <div class="float-left" style="width:400px;">
      <h4 class="kap">Samples</h4>
      <div class="table-responsive">
        <table class="table-striped">
          <thead>
            <tr>
              <th>User List</th>

            </tr>
          </thead>
          <tbody>
            {% for user in users %}
            <tr>
              {% if user not in friends %}
              <td>{{ container.container_id }}</td>
              <td>{{ user.username }}</td>
              <td>  <a href="{% url 'depot:change_friends' operation='add' pk=user.pk %}"  class="badge badge-primary" role="button">
                >>
              </a></td>
              {% endif %}
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>
    <div class="float-left" style="width:400px;">
      <h4 class="kap">Associated Users</h4>
      <div class="table-responsive">
        <table class="table-striped">
          <thead>
            <tr>
              <th>Samples</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              {% for friend in friends %}
              <td><a href="{% url 'depot:change_friends'  operation='remove' pk=friend.pk %}" class="badge badge-primary" role="button">
                <<
              </a></td>
              <td>{{ friend.username }}</td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </section>
  </div>
