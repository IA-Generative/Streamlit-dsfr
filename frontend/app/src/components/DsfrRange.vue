<script setup lang="ts">
import { ref } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrRange } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps.d.ts'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		// Slots
		label?: string
		hint?: string
		messages?: object
		// Props
		min?: number
		max?: number
		modelValue?: number
		id?: string
		lowerValue?: number
		message?: string
		prefix?: string
		suffix?: string
		small?: boolean
		hideIndicators?: boolean
		step?: number
		disabled?: boolean
	}>
>()

// Bind the input value to `value`
const value = ref<string>(props.args.modelValue || '')
const lastValue = ref(value.value)

let timeoutUpdate: NodeJS.Timeout | null = null

function setComponentValue()
{
	if (value.value !== lastValue.value)
	{
		lastValue.value = value.value
		Streamlit.setComponentValue(value.value)
	}
}

function onUpdateModelValue()
{
	if (timeoutUpdate)
	{
		clearTimeout(timeoutUpdate)
		timeoutUpdate = null
	}

	timeoutUpdate = setTimeout(setComponentValue, 200)
}
</script>

<template>
	<div class="component">
		<DsfrRange
			v-bind="props.args"
			:disabled="props.disabled || props.args.disabled"
			v-model="value"
			@update:modelValue="onUpdateModelValue"
		>
			<template #label v-if="props.args.label">
				{{ props.args.label }}
			</template>
			<template #hint v-if="props.args.hint">
				{{ props.args.hint }}
			</template>
			<template #messages v-if="props.args.messages">
				{{ props.args.messages }}
			</template>
		</DsfrRange>
	</div>
</template>

<style scoped>
.component :deep(.fr-range[data-fr-js-range]:after) {
	clip-path: polygon(
		var(--progress-left) 0,
		calc(var(--progress-right) - 24px) 0,
		calc(var(--progress-right) - 24px) 100%,
		var(--progress-left) 100%
	);
}
</style>
