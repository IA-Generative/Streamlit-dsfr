<script setup lang="ts">
import type { Component } from 'vue'

import WithStreamlitConnection from '../streamlit/WithStreamlitConnection.vue'

const props = defineProps<{
	component: Component
}>()

function streamlitStyle(theme: any)
{
	return {
		'--base': theme.base,
		'--primary-color': theme.primaryColor,
		'--background-color': theme.backgroundColor,
		'--secondary-background-color': theme.secondaryBackgroundColor,
		'--text-color': theme.textColor,
		'--font': theme.font,
	}
}
</script>

<template>
	<WithStreamlitConnection v-slot="{ width, args, disabled, theme }">
		<div class="component-wrapper" :style="streamlitStyle(theme)">
			<component :is="props.component" :width="width" :args="args" :disabled="disabled" :theme="theme" />
		</div>
	</WithStreamlitConnection>
</template>

<style scoped>
.component-wrapper {
	display: flex;
	flex-direction: column;
}
</style>
