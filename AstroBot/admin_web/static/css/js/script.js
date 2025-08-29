async function approveUser(userId) {
    await fetch('/admin/approve', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: userId })
    });
    location.reload();
}

async function rejectUser(userId) {
    await fetch('/admin/reject', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: userId })
    });
    location.reload();
}
